#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_stats():
    """ Print the accumulated statistics """
    print(f"File size: {total_size}")
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")


def handle_interrupt(signal, frame):
    """ Handle the keyboard interrupt (CTRL + C) """
    print_stats()
    sys.exit(0)


# Bind the interrupt signal to the handle_interrupt function
signal.signal(signal.SIGINT, handle_interrupt)

# Process the input
for line in sys.stdin:
    try:
        # Parse the line
        parts = line.split()
        if len(parts) < 7:
            continue

        ip_address = parts[0]
        date = parts[3] + " " + parts[4]
        request = parts[5] + " " + parts[6] + " " + parts[7]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Validate the request format
        if not request.startswith('"GET /projects/260 HTTP/1.1"'):
            continue

        # Accumulate the file size
        total_size += file_size

        # Increment the status code count
        if status_code in status_count:
            status_count[status_code] += 1

        line_count += 1

        # Print the stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

    except Exception:
        continue

# Print final statistics if the script ends without interruption
print_stats()
