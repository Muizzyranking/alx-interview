#!/usr/bin/python3
"""
Module to validate whether a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a
    valid UTF-8 encoding

    Args:
        data: list of integers representing data set

    Returns:
        True if data is a valid UTF-8 encoding, False otherwise
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to identify the significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Loop through each integer in the data array
    for byte in data:
        # If num_bytes is 0, determine how many
        # bytes the UTF-8 character should have
        if num_bytes == 0:
            # Check the number of leading 1's
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1 byte character
            if num_bytes == 0:
                continue

            # If the number of bytes is more than 4 or 1, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If it's a continuation byte, it must start with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes to check for the next characters
        num_bytes -= 1

    # If we finish checking and there are leftover bytes, return False
    return num_bytes == 0
