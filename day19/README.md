# Day 19 — Pytest fixtures

## Goal

Refactor service CLI tests using pytest fixtures.

## What I practiced

- pytest fixtures
- passing fixtures into test functions
- test data preparation
- cleaner assertions
- reducing repeated test code
- running automated tests with pytest

## Files

- `service_cli.py` — service CLI logic
- `services.json` — service state file
- `test_service_cli.py` — pytest tests with fixture

## Example fixture

```python
@pytest.fixture
def default_services():
    return {
        "nginx": "running",
        "postgres": "stopped",
        "redis": "running"
    }