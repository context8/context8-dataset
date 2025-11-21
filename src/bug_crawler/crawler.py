from __future__ import annotations

import asyncio
import json
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import AsyncIterator, Dict, Iterable, List, Optional, Tuple

import httpx

UTC = timezone.utc
ONE_SECOND = timedelta(seconds=1)


def parse_datetime(value: str) -> datetime:
    normalized = value.strip().replace("Z", "+00:00")
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC)


def format_datetime(dt: datetime) -> str:
    return dt.astimezone(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


@dataclass
class IssueRecord:
    id: int
    number: int
    repository: str
    title: str
    state: str
    labels: List[str]
    created_at: str
    updated_at: str
    closed_at: Optional[str]
    html_url: str
    window_start: str
    window_end: str

    @classmethod
    def from_api(cls, item: Dict, window: Tuple[datetime, datetime]) -> "IssueRecord":
        repo = item.get("repository_url", "").rstrip("/").split("/")[-2:]
        repo_full_name = "/".join(repo) if len(repo) == 2 else ""
        labels = [label.get("name", "") for label in item.get("labels", [])]
        return cls(
            id=item["id"],
            number=item["number"],
            repository=repo_full_name,
            title=item.get("title", ""),
            state=item.get("state", ""),
            labels=labels,
            created_at=item.get("created_at", ""),
            updated_at=item.get("updated_at", ""),
            closed_at=item.get("closed_at"),
            html_url=item.get("html_url", ""),
            window_start=format_datetime(window[0]),
            window_end=format_datetime(window[1]),
        )


class GitHubIssueCrawler:
    def __init__(
        self,
        *,
        token: str,
        label: str = "bug",
        state: str = "all",
        per_page: int = 100,
        max_results_per_query: int = 900,
        timeout: float = 20.0,
        max_retries: int = 3,
        user_agent: str = "bug-crawler/0.1",
    ) -> None:
        self.token = token
        self.label = label
        self.state = state
        self.per_page = per_page
        self.max_results_per_query = max_results_per_query
        self.max_retries = max_retries
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": user_agent,
            "X-GitHub-Api-Version": "2022-11-28",
        }
        limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
        self.client = httpx.AsyncClient(
            base_url="https://api.github.com",
            headers=self.headers,
            timeout=timeout,
            limits=limits,
        )

    async def close(self) -> None:
        await self.client.aclose()

    async def crawl(
        self,
        *,
        output_path: Path,
        start: datetime,
        end: datetime,
        append: bool = False,
    ) -> None:
        mode = "a" if append else "w"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open(mode, encoding="utf-8") as handle:
            await self._walk_range(handle, start, end)

    async def _walk_range(
        self, handle, start: datetime, end: datetime
    ) -> None:
        total_count = await self._count(start, end)
        sys.stdout.write(
            f"[range] {format_datetime(start)} .. {format_datetime(end)} -> {total_count} issues\n"
        )
        sys.stdout.flush()
        if total_count > self.max_results_per_query and start < end:
            mid = start + (end - start) / 2
            first_end = mid
            second_start = mid + ONE_SECOND
            await self._walk_range(handle, start, first_end)
            if second_start <= end:
                await self._walk_range(handle, second_start, end)
            return
        async for issue in self._fetch_window(start, end):
            handle.write(json.dumps(asdict(issue), ensure_ascii=False) + "\n")
            handle.flush()

    async def _count(self, start: datetime, end: datetime) -> int:
        params = self._build_params(start, end, page=1, per_page=1)
        data = await self._request(params)
        return int(data.get("total_count", 0))

    async def _fetch_window(
        self, start: datetime, end: datetime
    ) -> AsyncIterator[IssueRecord]:
        page = 1
        while True:
            params = self._build_params(start, end, page=page, per_page=self.per_page)
            data = await self._request(params)
            items = data.get("items", [])
            if not items:
                return
            for item in items:
                if "pull_request" in item:
                    continue
                yield IssueRecord.from_api(item, (start, end))
            page += 1
            if page > 10_000:
                return

    def _build_params(
        self, start: datetime, end: datetime, *, page: int, per_page: int
    ) -> Dict:
        query = (
            f"is:issue is:public label:{self.label} "
            f"state:{self.state} "
            f"created:{format_datetime(start)}..{format_datetime(end)}"
        )
        return {
            "q": query,
            "sort": "created",
            "order": "asc",
            "per_page": per_page,
            "page": page,
        }

    async def _request(self, params: Dict) -> Dict:
        attempt = 0
        while True:
            attempt += 1
            response = await self.client.get("/search/issues", params=params)
            if response.status_code in (403, 429):
                wait_for = self._next_retry_delay(response)
                sys.stdout.write(f"[rate-limit] sleeping {wait_for:.1f}s\n")
                sys.stdout.flush()
                await asyncio.sleep(wait_for)
                continue
            try:
                response.raise_for_status()
            except httpx.HTTPStatusError as exc:
                if attempt <= self.max_retries:
                    await asyncio.sleep(min(2**attempt, 10))
                    continue
                raise RuntimeError(
                    f"GitHub API error {exc.response.status_code}: {exc.response.text}"
                ) from exc
            return response.json()

    def _next_retry_delay(self, response: httpx.Response) -> float:
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                return float(retry_after)
            except ValueError:
                pass
        remaining = response.headers.get("X-RateLimit-Remaining")
        reset = response.headers.get("X-RateLimit-Reset")
        if remaining == "0" and reset:
            try:
                reset_at = int(reset)
                now = int(time.time())
                return max(reset_at - now + 1, 1)
            except ValueError:
                return 30.0
        return 10.0


async def run_crawl(
    *,
    token: str,
    output: Path,
    start: datetime,
    end: datetime,
    label: str = "bug",
    state: str = "all",
    per_page: int = 100,
    max_results_per_query: int = 900,
    append: bool = False,
) -> None:
    crawler = GitHubIssueCrawler(
        token=token,
        label=label,
        state=state,
        per_page=per_page,
        max_results_per_query=max_results_per_query,
    )
    try:
        await crawler.crawl(
            output_path=output,
            start=start,
            end=end,
            append=append,
        )
    finally:
        await crawler.close()
