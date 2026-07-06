# Day 13 — Improved CLI service tool

## Goal

Improve the CLI-style service status tool by adding service control commands.

## Topics

- Command-line arguments
- `sys.argv`
- CLI command parsing
- Dictionary lookup
- Updating dictionary values
- Basic command validation
- Basic error handling

## Project

`service_cli.py`

A simple CLI-style Python tool for listing services, checking service status, and changing service state during runtime.

## Supported commands

List all services:

```bash
python3 service_cli.py list