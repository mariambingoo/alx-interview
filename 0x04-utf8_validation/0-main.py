#!/usr/bin/python3
"""
Testing UTF-8 Validation
"""

is_valid_utf8 = __import__('0-validate_utf8').is_valid_utf8

# Testing single-byte ASCII characters
data = [65]
print(is_valid_utf8(data))  # Expected output: True

# Testing a sequence of ASCII characters
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(is_valid_utf8(data))  # Expected output: True

# Testing a sequence with an invalid byte
data = [229, 65, 127, 256]
print(is_valid_utf8(data))  # Expected output: False

