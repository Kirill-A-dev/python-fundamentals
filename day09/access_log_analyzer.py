logs = [
    "INFO User login successful",
    "ERROR Database connection failed",
    "WARNING Disk space is low",
    "INFO Backup completed",
    "ERROR Timeout while connecting to API",
    "CRITICAL Server is down",
    "INFO User logout",
]
stats = {
    "INFO": 0,
    "ERROR": 0,
    "WARNING": 0,
    "CRITICAL": 0,
}
for log in logs:
    parts = (log.split())
    level = parts[0]
    if level in stats:
        stats[level] += 1
    
print("Log report:")
for level , count in stats.items():
    print(f'{level}: {count}')