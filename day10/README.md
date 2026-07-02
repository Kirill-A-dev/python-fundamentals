# Day 10 — File Log Analyzer Practice

## Goal

Practice reading log data from an external file and generating a simple report.

The script reads log lines from `server.log`, extracts the log level from each line, counts the number of `INFO`, `ERROR`, `WARNING`, and `CRITICAL` messages, and prints a summary report.

## Topics practiced

- Reading files with `open()`
- Using `with` for safe file handling
- Iterating over file lines
- `strip()`
- `split()`
- Dictionaries
- `dict.items()`
- Basic log analysis

## Files

- `server.log` — sample log file.
- `file_log_analyzer.py` — reads the log file and prints a log level summary.

## Expected output

```text
Log report:
INFO: 3
ERROR: 2
WARNING: 1
CRITICAL: 1
