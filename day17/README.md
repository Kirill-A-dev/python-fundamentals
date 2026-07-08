# Day 17 — Basic Tests for Service CLI

## Goal

Add basic automated tests for the service CLI project.

## What I practiced

- Basic testing
- `assert`
- Test functions
- Regression testing
- Testing function behavior
- Testing JSON error handling
- Manual test runner

## Files

- `service_cli.py` — CLI application
- `services.json` — JSON data file
- `test_service_cli.py` — basic test script

## Tests

- `test_start_service()`
- `test_stop_service()`
- `test_reset_services()`
- `test_load_services_broken_json()`
- `test_load_services_wrong_type()`
- `test_load_services_missing_file()`
- `test_load_services_valid_json()`

## Run tests

```bash
python3 test_service_cli.py