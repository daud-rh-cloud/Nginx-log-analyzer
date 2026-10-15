# nginx-log-analyzer

A small Python tool that reads an NGINX access log and prints a report:
status codes, 5xx error rate, top IPs, top paths, and requests per hour.
Lines that can't be parsed are skipped and listed instead of crashing the program.

Plain Python 3, no external libraries.

> **Status:** learning project, work in progress.

## Example input

Each line is one request in NGINX's *combined* log format:

```
192.168.1.10 - - [05/Oct/2026:13:00:01 +0200] "GET /api/users HTTP/1.1" 200 512 "-" "curl/8.4.0"
```

## Example output

```
=== logsentry report: big.log ===
Status codes:
200     26
404     5
...
5xx Error rate: 12.50%

Top IPs:
198.51.100.23   10
192.0.2.88      8
...

Requests per hour:
07/Oct/2026:08    1
07/Oct/2026:09    21
...
```

 

The log file path is set at the top of `main.py`. Change it to point at your own log.

## Project structure

| File | What it does |
|---|---|
| `main.py` | Entry point: reads the file and connects the parts |
| `Parsers.py` | Splits each raw line into fields and rejects malformed lines |
| `Models.py` | `LogEntry`: holds one parsed line |
| `Analyzers.py` | Counts status codes, error rate, top IPs, top paths, requests per hour |
| `Reporter.py` | Prints the report |

## How parsing works

Each line is first split on the `"` character. A valid line gives exactly 7 pieces,
so lines with any other count are rejected. Each piece is then split on spaces to get
the IP, timestamp, method, path, status, and bytes. Splitting on `"` first means user
agents containing spaces, such as `Mozilla/5.0 (Windows NT 10.0; ...)`, don't break the parser.


