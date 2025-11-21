# Bug Issue Crawler

利用 GitHub Search API 抓取所有公开仓库中带有特定标签（默认 `bug`）的 Issue，数据以 JSONL 形式保存，便于后续做数据处理或分析。

## 准备

- Python 3.10+
- 依赖：`pip install -r requirements.txt`
- GitHub Token：环境变量 `GITHUB_TOKEN`，或运行时通过 `--token` 传入。未认证的请求会被速率限制。

## 基本用法

```bash
PYTHONPATH=src python -m bug_crawler.cli \
  --start 2024-01-01 \
  --end 2024-01-07 \
  --output data/bug-issues-20240101-20240107.jsonl
```

关键参数：

- `--label`：过滤标签，默认 `bug`。
- `--state`：`open` / `closed` / `all`，默认 `all`。
- `--per-page`：单次请求条数（<=100），默认 100。
- `--max-results`：单个时间窗口最多抓取条数，超过会自动把窗口一分为二避免 Search API 1000 上限。
- `--append`：输出文件已存在时追加写入。

## 工作方式

1. 按时间窗口构造查询 `is:issue is:public label:<label> state:<state> created:<start>..<end>`。
2. 若窗口结果数超过 `--max-results`，自动二分时间窗口递归抓取，避免 Search API 1000 条限制。
3. 对每页结果逐条写入 JSONL，字段包含 Issue 元数据和所属查询窗口。
4. 检测 `Retry-After / X-RateLimit-Reset` 自动等待，尽量不中断。

## 本地校验

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

## 数据字段

每行 JSON 形如：

```json
{
  "id": 1,
  "number": 42,
  "repository": "owner/repo",
  "title": "Found a bug",
  "state": "open",
  "labels": ["bug"],
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-02T00:00:00Z",
  "closed_at": null,
  "html_url": "https://github.com/owner/repo/issues/42",
  "window_start": "2024-01-01T00:00:00Z",
  "window_end": "2024-01-07T00:00:00Z"
}
```

## 注意事项

- Search API 仍有总量与速率限制，真正意义的“所有公开仓库 Bug Issue”需要极长时间与充足配额。
- 建议按日期递增抓取，持续追加到同一 JSONL。
- 若窗口非常大却包含超过 1000 条 Issue，并且时间粒度已无法再切分，会记录当前窗口并继续尝试（结果可能缺失），可缩短时间范围以提高完整度。
