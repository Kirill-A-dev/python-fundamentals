level_counts = {}
service_counts = {}
with open("structured_logs.log", "r") as file:
    for line in file:
        clean_line = line.strip()
        parts = clean_line.split()
        date = parts[0]
        time = parts[1]
        level = parts[2]
        service = parts[3]
        message = " ".join(parts[4:])
        print(f'\ndate: {date}')
        print(f'time: {time}')
        print(f'level: {level}')
        print(f'service: {service}')
        print(f'message: {message}')        
        if level not in level_counts:
            level_counts[level] = 1
        else:
            level_counts[level] += 1
        if service not in service_counts:
            service_counts[service] = 1
        else:
            service_counts[service] += 1
print("\nLog level summary:")
for level , number in level_counts.items():
    print(f'{level}: {number}')
print("\nService summary:")
for service , number in service_counts.items():
    print(f'{service}: {number}')
