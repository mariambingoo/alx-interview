#!/usr/bin/python3
"""
log parsing script
"""

import sys
import re
from collections import Counter


def output(log: dict) -> None:
    """
    Helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


def parse_line(line: str, regex: re.Pattern, log: dict) -> bool:
    """
    Parse a single log line and update log stats
    Returns True if the line was valid, False otherwise.
    """
    match = regex.fullmatch(line)
    if not match:
        return False

    
    code = match.group(1)
    file_size = match.group(2)

    # Update file size
    log["file_size"] += int(file_size)

    # Update status code frequency
    if code.isdecimal():
        log["code_frequency"][code] += 1

    return True


if __name__ == "__main__":
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] '
        r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'  
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": Counter()
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            if parse_line(line, regex, log):
                line_count += 1

                # Output stats every 10 lines
                if line_count % 10 == 0:
                    output(log)
    except KeyboardInterrupt:
        pass
    finally:
        output(log)

