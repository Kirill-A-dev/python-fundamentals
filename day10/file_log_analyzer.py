stats = {
    "INFO": 0,
    "ERROR": 0,
    "WARNING": 0,
    "CRITICAL": 0,
}
with open("server.log", "r") as file:
    for line in file:
        clean_line = line.strip()
        parts = clean_line.split()
        level = parts[0]
        if level in stats:
            stats[level] += 1
print("Log report:")
for level , count in stats.items():
    print(f'{level}: {count}')