"""
Problem 02: Count Requests per User from Logs

You receive application logs as an iterator of lines. Each line is a JSON
string with at least a `user_id` field, for example:

{"timestamp": "2025-12-11T19:00:00Z", "user_id": 42, "path": "/login"}
{"timestamp": "2025-12-11T19:00:01Z", "user_id": 17, "path": "/dashboard"}
{"timestamp": "2025-12-11T19:00:02Z", "user_id": 42, "path": "/settings"}

Write a function:

    def count_requests_per_user(lines):
        ...

that:
- Takes `lines`, an iterator (or list) of log lines (strings).
- Parses each line as JSON.
- Counts how many requests each `user_id` has made.
- Returns a dictionary mapping `user_id` -> request count.

Constraints:
- The log file can be very large, so you must not read all lines
  into memory at once. Process line by line.
- Lines that fail JSON parsing should be skipped (do not crash).
"""
import json
from collections import defaultdict

import json
from collections import defaultdict


def count_requests_per_user(lines):
    counts = defaultdict(int)
    for line in lines:
        try:
            data = json.loads(line)
            user_id = data.get("user_id")
            if user_id is not None:
                counts[user_id] += 1
        except json.JSONDecodeError:
            # Skip malformed lines
            continue
    return counts


if __name__ == "__main__":
    lines = [
        '{"timestamp": "2025-12-11T19:00:00Z", "user_id": 42, "path": "/login"}',
        '{"timestamp": "2025-12-11T19:00:01Z", "user_id": 17, "path": "/dashboard"}',
        '{"timestamp": "2025-12-11T19:00:02Z", "user_id": 42, "path": "/settings"}',
    ]

    print(count_requests_per_user(lines))
    # Expected: defaultdict(int, {42: 2, 17: 1})

    print(count_requests_per_user(lines))
    print(count_requests_per_user(lines))   