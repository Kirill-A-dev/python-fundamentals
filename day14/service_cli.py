import sys
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICES_FILE = os.path.join(BASE_DIR, "services.json")

DEFAULT_SERVICES = {
    "nginx": "running",
    "postgres": "stopped",
    "redis": "running"
}
def load_services():
    if os.path.exists(SERVICES_FILE):
        with open(SERVICES_FILE, "r") as file:
            return json.load(file)
    return DEFAULT_SERVICES.copy()


def save_services(services):
    with open(SERVICES_FILE, "w") as file:
        json.dump(services, file, indent=4)

services = load_services()  

commands = ["status" , "start" , "stop"]
args = sys.argv
if  len(args) > 3 or len(args) < 2:
    print("Usage: ")
    print("  python3 service_cli.py list")
    print("  python3 service_cli.py status <service>")
    print("  python3 service_cli.py start <service>")
    print("  python3 service_cli.py stop <service>")
    sys.exit()
if len(args) == 2:
    command = args[1]
    if command == "list":
        for service , status in services.items():
            print(f'{service}: {status}')
    else:
        print("Invalid command")
        sys.exit()
if len(args) == 3:
    command = args[1]
    if command in commands:
        service = args[2]
        if service in services:
            if command == "status":            
                print(f'{service} is {services[service]}')
            elif command == "start": 
                services[service] = "running"
                save_services(services)          
                print(f'{service} started')           
            elif command == "stop":
                services[service] = "stopped"
                save_services(services)            
                print(f'{service} stopped')
        else:
                print("Service not found")
    else:
        print("Invalid command")