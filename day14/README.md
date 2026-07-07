# Day 14 — Saving service state to JSON

## Goal

Improve the CLI service tool by saving service statuses to a JSON file.

## Topics

- JSON files
- `json.load()`
- `json.dump()`
- Reading data from a file
- Saving updated data to a file
- Persistent service state

## Project

`service_cli.py`

A CLI-style Python tool for listing services, checking service status, starting services, stopping services, and saving changes to `services.json`.

## Supported commands

List all services:

```bash
python3 service_cli.py list