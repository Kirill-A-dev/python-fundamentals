services = {
    "nginx" : "running",
    "postgres" : "stopped",
    "redis" : "running"
}
parts = input().split()
length = len(parts)
if length == 1:
    command = parts[0]
    if command == "list":
        for service , status in services.items():
            print(f'{service} is {status}')
    elif command == "status":
        print("Usage: status <service>")
    else:
        print("Invalid command")
elif length == 2:
    command = parts[0]
    service = parts[1]
    if command == "status":
        if service in services:
            print(f'{service} is {services[service]}')
        else:
            print("Service not found")
    else:
        print("Invalid command")
else:
    print("Usage: status <service> or list")