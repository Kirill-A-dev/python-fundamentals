import os
import json
import pytest

from service_cli import start_service, stop_service, reset_services, load_services

@pytest.fixture
def default_services():
    return {
        "nginx": "running",
        "postgres": "stopped",
        "redis": "running"
    }

def test_start_service():
    services = {"nginx": "stopped"}

    start_service(services, "nginx")

    assert services["nginx"] == "running"

def test_stop_service():
    services = {"nginx": "running"}
    
    stop_service(services, "nginx")

    assert services["nginx"] == "stopped"

def test_reset_services(default_services):
    services = reset_services()
    assert services == default_services
    
def test_load_services_broken_json(default_services):
    with open("services.json", "w") as file:
        file.write("{broken json")
    services = load_services()
    assert isinstance(services, dict)
    assert services == default_services

def test_load_services_wrong_type(default_services):
    with open("services.json", "w") as file:
        file.write("['nginx' : 'postgres']")
    services = load_services()
    assert isinstance(services, dict)
    assert services == default_services

def test_load_services_missing_file(default_services):
    if os.path.exists("services.json"):
       os.remove("services.json")
    services = load_services()
    assert isinstance(services, dict)
    assert services == default_services

def test_load_services_valid_json():
    test_data = {
    "nginx": "stopped",
    "postgres": "running",
    "redis": "stopped"
}
    with open("services.json", "w") as file:
        json.dump(test_data, file)
    services = load_services()
    assert isinstance(services, dict)
    assert test_data == services

