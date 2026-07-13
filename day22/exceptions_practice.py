services = {
    "nginx": "running",
    "postgres": "stopped"
}

class InvalidStatusError(Exception):
    pass

class ServiceNotFoundError(Exception):
    pass

def show_service(service):
    if service not in services:
        raise ServiceNotFoundError(f"Service '{service}' not found")
    print(f'{service} is {services[service]}')

def change_status(service, new_status):
    if service not in services:
        raise ServiceNotFoundError(f"Service '{service}' not found")    
    if new_status not in ["running","stopped"]:
        raise InvalidStatusError(f"Invalid status '{new_status}'")
    services[service] = new_status
    print(f'{service} is {new_status}')


try:
    show_service("nginx")    
except ServiceNotFoundError as error:
    print(f'Error: {error}')

try:
    show_service("mysql")    
except ServiceNotFoundError as error:
    print(f'Error: {error}')


try:    
    change_status("postgres","running")
except ServiceNotFoundError as error:
    print(f'Error: {error}')
except InvalidStatusError as error:
    print(f'Error: {error}')

try:
    change_status("nginx","broken")
except ServiceNotFoundError as error:
    print(f'Error: {error}')
except InvalidStatusError as error:
    print(f'Error: {error}')

print("Programm finished")