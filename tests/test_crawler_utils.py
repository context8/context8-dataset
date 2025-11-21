import asyncio
import unittest

from bug_crawler.crawler import GitHubIssueCrawler, format_datetime, parse_datetime


class CrawlerHelpersTest(unittest.TestCase):
    def test_parse_and_format_roundtrip(self) -> None:
        dt = parse_datetime("2024-01-01T12:34:56Z")
        self.assertEqual(format_datetime(dt), "2024-01-01T12:34:56Z")

    def test_build_params_contains_expected_query(self) -> None:
        crawler = GitHubIssueCrawler(token="dummy-token")
        start = parse_datetime("2024-01-01T00:00:00Z")
        end = parse_datetime("2024-01-02T00:00:00Z")
        params = crawler._build_params(start, end, page=1, per_page=50)
        query = params["q"]
        self.assertIn("label:bug", query)
        self.assertIn("state:all", query)
        self.assertIn(
            "created:2024-01-01T00:00:00Z..2024-01-02T00:00:00Z",
            query,
        )
        self.assertEqual(params["per_page"], 50)
        asyncio.run(crawler.close())


if __name__ == "__main__":
    unittest.main()
