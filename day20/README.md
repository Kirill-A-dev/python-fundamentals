# Day 20 — Logging

## Learned

- Python `logging` module
- Log levels:
  - DEBUG
  - INFO
  - WARNING
  - ERROR
  - CRITICAL
- `logging.basicConfig()`
- Log formatting
- Writing logs to a file
- Append mode with `filemode="a"`
- Using logs together with CLI output
- Logging successful operations and errors
- Absolute paths for log files
- Testing error recovery

## Project

Extended the service manager CLI with file logging.

The application logs:

- successful loading of services;
- service status changes;
- unknown commands;
- missing services;
- missing or invalid JSON files;
- restoration of default service values.

## Tests

```bash
pytest -v