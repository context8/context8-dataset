import argparse
import asyncio
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from .crawler import format_datetime, parse_datetime, run_crawl


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Crawl GitHub public issues labeled as bug into JSONL."
    )
    parser.add_argument("--token", help="GitHub token; falls back to GITHUB_TOKEN env.")
    parser.add_argument(
        "--start",
        required=True,
        help="ISO8601 start datetime (e.g. 2024-01-01 or 2024-01-01T00:00:00Z).",
    )
    parser.add_argument(
        "--end",
        help="ISO8601 end datetime; defaults to now UTC if omitted.",
    )
    parser.add_argument("--output", required=True, help="Path to output JSONL file.")
    parser.add_argument("--label", default="bug", help="Label to filter, default bug.")
    parser.add_argument(
        "--state",
        default="all",
        choices=["open", "closed", "all"],
        help="Issue state filter.",
    )
    parser.add_argument(
        "--per-page",
        type=int,
        default=100,
        help="Items per request (max 100).",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=900,
        help="Maximum issues to pull per search window before splitting.",
    )
    parser.add_argument(
        "--append",
        action="store_true",
        help="Append to output file instead of overwriting.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    token = args.token or os.getenv("GITHUB_TOKEN")
    if not token:
        parser.error("GitHub token is required (flag --token or env GITHUB_TOKEN).")

    start = parse_datetime(args.start)
    end = parse_datetime(args.end) if args.end else datetime.now(timezone.utc)
    if end <= start:
        parser.error("end must be after start.")

    output_path = Path(args.output)
    if output_path.exists() and not args.append:
        parser.error(f"{output_path} exists, use --append to extend it.")

    sys.stdout.write(
        f"[config] label={args.label} state={args.state} "
        f"range={format_datetime(start)}..{format_datetime(end)} "
        f"per_page={args.per_page} max_results={args.max_results}\n"
    )
    sys.stdout.flush()

    asyncio.run(
        run_crawl(
            token=token,
            output=output_path,
            start=start,
            end=end,
            label=args.label,
            state=args.state,
            per_page=args.per_page,
            max_results_per_query=args.max_results,
            append=args.append,
        )
    )


if __name__ == "__main__":
    main()
