import sys
import json
import os
import logging



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICES_FILE = os.path.join(BASE_DIR, "services.json")
LOG_FILE = os.path.join(BASE_DIR, "app.log")

DEFAULT_SERVICES = {
    "nginx": "running",
    "postgres": "stopped",
    "redis": "running"
}

def setup_config():
    logging.basicConfig(
         filename = LOG_FILE,
         filemode = 'a',
         datefmt='%Y-%m-%d %H:%M:%S',
         format = '%(asctime)s - %(levelname)s - %(message)s',
         level = logging.INFO
     )

def reset_services():
    print("Warning: services.json was missing or invalid. Resetting to default services.")
    save_services(DEFAULT_SERVICES)
    logging.warning("Services reset to default values")
    return DEFAULT_SERVICES.copy()
    
def load_services():
    try:
        with open(SERVICES_FILE, "r") as file:
            services = json.load(file)
            if not isinstance(services, dict):
                return reset_services() 
            logging.info("Services loaded successfully")
            return services           
    except FileNotFoundError:
        logging.error(f'Services file not found: {SERVICES_FILE}')
        return reset_services()    
    except json.JSONDecodeError:
        logging.error("Failed to decode services JSON")
        return reset_services()
    
def save_services(services):
    with open(SERVICES_FILE, "w") as file:
        json.dump(services, file, indent=4)

def show_usage():
    print("Usage:")
    print("  python3 service_cli.py list")
    print("  python3 service_cli.py status <service>")
    print("  python3 service_cli.py start <service>")
    print("  python3 service_cli.py stop <service>")

def list_services(services):
    for service, status in services.items():
        print(f"{service}: {status}")

def show_status(services, service):
    print(f"{service} is {services[service]}")

def start_service(services, service):
    services[service] = "running"
    save_services(services)
    logging.info(f'Service {service} changed status to running')          
    print(f'{service} started')

def stop_service(services, service):
    services[service] = "stopped"
    save_services(services)
    logging.info(f'Service {service} changed status to stopped')           
    print(f'{service} stopped')

def main():
    setup_config()

    services = load_services()

    commands = ["status", "start", "stop"]
    args = sys.argv

    if len(args) > 3 or len(args) < 2:
        show_usage()
        sys.exit()

    if len(args) == 2:
        command = args[1]

        if command == "list":
            list_services(services)
        else:
            print("Invalid command")
            logging.warning(f'Unknown command: {command}')
            sys.exit()

    if len(args) == 3:
        command = args[1]

        if command in commands:
            service = args[2]

            if service in services:
                if command == "status":
                    show_status(services, service)
                elif command == "start":
                    start_service(services, service)
                elif command == "stop":
                    stop_service(services, service)
            else:
                print("Service not found")
                logging.warning(f'Service not found: {service}')
                sys.exit()
        else:
            print("Invalid command")
            logging.warning(f'Unknown command: {command}')
            sys.exit()

if __name__ == "__main__":
    main()