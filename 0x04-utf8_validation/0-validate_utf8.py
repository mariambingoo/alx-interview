#!/usr/bin/python3
"""UTF-8 Encoding Validation"""


def count_leading_ones(byte):
    """Counts the number of leading '1' bits in a byte."""
    ones_count = 0
    mask = 1 << 7
    while mask & byte:
        ones_count += 1
        mask >>= 1
    return ones_count


def is_valid_utf8(byte_sequence):
    """Checks if a given byte sequence is valid UTF-8 encoded data."""
    remaining_bytes = 0
    for byte in byte_sequence:
        if remaining_bytes == 0:
            # Count leading '1's to determine the byte length of the UTF-8 character.
            remaining_bytes = count_leading_ones(byte)
            
            # Single-byte character (format: 0xxxxxxx)
            if remaining_bytes == 0:
                continue
            
            # UTF-8 characters must be 1 to 4 bytes long
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            # Check if the current byte is of the form 10xxxxxx
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0

