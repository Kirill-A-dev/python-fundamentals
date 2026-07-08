# Day 15 — Refactor Service CLI with Functions

## Goal

Refactor the Day 14 service CLI project by moving repeated logic into functions.

## What I practiced

- Python functions
- Code organization
- Reusing logic
- CLI command handling
- JSON loading and saving
- Project structure

## Files

- `service_cli.py` — CLI application for managing service statuses
- `services.json` — JSON file used for persistent service data

## Commands

```bash
python3 service_cli.py list
python3 service_cli.py status nginx
python3 service_cli.py start nginx
python3 service_cli.py stop nginx