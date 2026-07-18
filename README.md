# Terminal-Bench 2 Harbor Task: Log Report

A fixed Terminal-Bench 2 (Harbor) task that parses an Apache-style access log and generates a JSON summary report.

## Task

Analyze `/app/access.log` and create `/app/report.json`:

```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
```

## Run

From the directory containing `log-report/`:

```bash
harbor run -p log-report -a oracle
```

Expected: `Reward: 1.0`

Test the no-op agent:

```bash
harbor run -p log-report --agent nop
```

Expected: `Reward: 0.0`

## Verification

The verifier checks the actual JSON values, not just whether the file exists.

Verifier outputs:

- `/logs/verifier/reward.txt`
- `/logs/verifier/ctrf.json`

The environment uses a digest-pinned base image and does not leak the reference solution into the agent environment.
