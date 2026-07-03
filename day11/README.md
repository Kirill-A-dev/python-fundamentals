# Day11 — Dictionaries and structured log parsing

## Goals

- Practice Python dictionaries
- Build a simple service status checker
- Parse structured log lines from a file
- Extract fields from each log entry
- Count log levels using a dictionary
- Count services using a dictionary

## Files

- `service_status.py` — simple service status checker
- `structured_logs.log` — example structured log file
- `structured_log_parser.py` — parser for structured log lines

---

## 1. Service status checker

File:

```text
service_status.py
```

The script stores service statuses in a dictionary:

```python
services = {
    "nginx": "running",
    "postgres": "stopped",
    "redis": "running"
}
```

Supported commands:

```text
list
status <service>
```

Run:

```bash
python3 service_status.py
```

Examples:

```text
list
```

Expected output:

```text
nginx is running
postgres is stopped
redis is running
```

Example:

```text
status nginx
```

Expected output:

```text
nginx is running
```

Example:

```text
status apache
```

Expected output:

```text
Service not found
```

Invalid command examples:

```text
hello
```

Expected output:

```text
Invalid command
```

```text
status
```

Expected output:

```text
Usage: status <service>
```

```text
status nginx extra
```

Expected output:

```text
Usage: status <service> or list
```

What this script practices:

- dictionaries
- checking if a key exists in a dictionary
- command parsing with `.split()`
- `if / elif / else`
- loops over dictionaries with `.items()`

---

## 2. Structured log parser

Files:

```text
structured_logs.log
structured_log_parser.py
```

Example log line:

```text
2026-07-02 12:30:01 INFO auth User login successful
```

The parser extracts:

- date
- time
- level
- service
- message

Run:

```bash
python3 structured_log_parser.py
```

Example parsed output:

```text
date: 2026-07-02
time: 12:30:01
level: INFO
service: auth
message: User login successful
```

Example summary:

```text
Log level summary:
INFO: 1
ERROR: 1
WARNING: 1
CRITICAL: 1

Service summary:
auth: 1
database: 1
system: 1
server: 1
```

What this script practices:

- reading files with `with open(...)`
- iterating over file lines
- `.strip()`
- `.split()`
- `" ".join(...)`
- extracting fields by index
- dictionary counters
- summary output

---

## Key concepts

### Dictionary lookup

```python
if service in services:
    print(services[service])
```

### Dictionary counter

```python
if level not in level_counts:
    level_counts[level] = 1
else:
    level_counts[level] += 1
```

### Splitting structured data

```python
parts = line.split()

date = parts[0]
time = parts[1]
level = parts[2]
service = parts[3]
message = " ".join(parts[4:])
```