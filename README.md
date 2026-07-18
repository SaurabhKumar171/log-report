# Terminal-Bench 2 Harbor Task: Log Report

A fixed Terminal-Bench 2 (Harbor) task that parses an Apache-style access log and generates a JSON summary report.

## Task

The agent must analyze:

`/app/access.log`

and create:

`/app/report.json`

The report must contain:

```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}