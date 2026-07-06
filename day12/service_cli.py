import sys
services = {
    "nginx" : "running",
    "postgres" : "stopped",
    "redis" : "running"
}
args = sys.argv
if  len(args) > 3 or len(args) < 2:
    print("Usage: ")
    print("  python3 service_cli.py list")
    print("  python3 service_cli.py status <service>")
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
    if command == "status":
        service = args[2]
        if service in services:
            print(f'{service} is {services[service]}')
        else:
            print("Service not found")
    else:
        print("Invalid command")






