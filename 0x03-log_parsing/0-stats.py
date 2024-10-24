#!/usr/bin/env python3
import sys
import signal

total_size, line_count = 0, 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_count):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")

def parse_line(line):
    global total_size
    parts = line.split()
    if len(parts) >= 7 and parts[5] == '"GET' and parts[6] == '/projects/260' and parts[7] == 'HTTP/1.1"':
        try:
            status_code, file_size = int(parts[-2]), int(parts[-1])
            total_size += file_size
            if status_code in status_count:
                status_count[status_code] += 1
        except ValueError:
            pass

def handle_interrupt(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

for line in sys.stdin:
    parse_line(line.strip())
    line_count += 1
    if line_count % 10 == 0:
        print_stats()

print_stats()
