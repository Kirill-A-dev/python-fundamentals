servers = [
    {"name": "web-01", "status": "running", "cpu": 35},
    {"name": "db-01", "status": "running", "cpu": 72},
    {"name": "cache-01", "status": "stopped", "cpu": 0},
    {"name": "worker-01", "status": "running", "cpu": 91},
]
with open("server_report.txt", "w") as file:
    for server in servers:
        if server["status"] == "stopped":
            alert = "server is down"
        elif server["cpu"] > 80:
            alert = "high cpu usage"
        else:
            alert = "ok"
        file.write(f'{server["name"]}: status = {server["status"]}, cpu = {server["cpu"]}%, alert = {alert}\n')

print("Server status added")