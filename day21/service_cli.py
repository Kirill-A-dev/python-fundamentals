import json
import os
import logging
import argparse



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICES_FILE = os.path.join(BASE_DIR, "services.json")
LOG_FILE = os.path.join(BASE_DIR, "app.log")

DEFAULT_SERVICES = {
    "nginx": "running",
    "postgres": "stopped",
    "redis": "running"
}


def create_parser():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
    "command", 
    choices=["list", "status", "start", "stop"],
    help="Command to execute"
    )
    parser.add_argument(
    "service",
    nargs="?",
    help="Service name"
    )
        
    return parser
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
    parser = create_parser()
    args = parser.parse_args()
    if args.command == "list":
        list_services(services)
        return        
    if args.service is None:
        parser.error("Service is required")
    if args.service not in services:
        logging.warning(f'Service not found: {args.service}')
        parser.error(f"Service not found: {args.service}")
    if args.command == "status":
        show_status(services, args.service)
    elif args.command == "start":
        start_service(services, args.service)
    elif args.command == "stop":
        stop_service(services, args.service)       

if __name__ == "__main__":
    main()