#!/usr/bin/python3
"""
This is a script that reads stdin line by line
and computes metrics
"""
import signal


def calculate_metrics(log_lines):
    """Function documentation
    """
    total_size = 0
    status_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    for line in log_lines:
        parts = line.split()
        if len(parts) >= 8:
            status_code = int(parts[7])
            file_size = int(parts[8])
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
    return total_size, status_counts


def print_metrics(total_size, status_counts):
    """Function documentation
    """
    print("Total file size:", total_size)
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")


log_lines = []
log_line_counter = 0


def handler(signum, frame):
    """Function documentation
    """
    global log_line_counter, log_lines
    if log_line_counter > 0:
        total_size, status_counts = calculate_metrics(log_lines)
        print_metrics(total_size, status_counts)
    log_lines = []
    log_line_counter = 0


signal.signal(signal.SIGINT, handler)

while True:
    log_line = input()
    log_lines.append(log_line)
    log_line_counter += 1
    if log_line_counter >= 10:
        total_size, status_counts = calculate_metrics(log_lines)
        print_metrics(total_size, status_counts)
        log_lines = []
        log_line_counter = 0
