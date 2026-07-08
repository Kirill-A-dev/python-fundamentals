# Day 16 — Add Error Handling to Service CLI

## Goal

Improve the Day 15 service CLI project by adding safer error handling for JSON loading and file operations.

The program should not crash if `services.json` is missing, empty, invalid, or contains data in the wrong format.

## What I practiced

- `try`
- `except`
- `FileNotFoundError`
- `json.JSONDecodeError`
- Type checking with `isinstance()`
- Defensive programming
- Safer JSON loading
- CLI reliability

## Files

- `service_cli.py` — CLI application for managing service statuses
- `services.json` — JSON file used for persistent service data

## Commands

```bash
python3 service_cli.py list
python3 service_cli.py status nginx
python3 service_cli.py start nginx
python3 service_cli.py stop nginx