#!/usr/bin/python3
"""
Log parsing script
"""

import sys
import re

def output(log: dict) -> None:
    """
    Helper function to display statistics
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print("{}: {}".format(code, log["code_frequency"][code]))

if __name__ == "__main__":
    # Regular expression to match log format
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'  # match status code and file size
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
        }
    }

    try:
        for line in sys.stdin:
            line = line.strip()  
            match = regex.fullmatch(line)  
            
            if match:
                line_count += 1
                code = match.group(1)  
                file_size = int(match.group(2))  

                # Update the total file size
                log["file_size"] += file_size

                # Update the status code frequency
                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                # Every 10 lines, output the stats
                if line_count % 10 == 0:
                    output(log)

    except KeyboardInterrupt:
        pass  

    finally:
        output(log)

