#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""

import sys

# Initialize metrics
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """Prints the current statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Split the line by spaces
            parts = line.split()
            # Extract status code and file size
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size
            total_file_size += file_size

            # Update status code counts
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        except (IndexError, ValueError):
            # Skip lines that don't match the expected format
            continue

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print statistics when interrupted by CTRL + C
    print_stats()
    raise

# Print final statistics if the loop ends normally
print_stats()
