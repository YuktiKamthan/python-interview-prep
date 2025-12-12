"""
Problem 01: Dedupe Users by user_id

You receive a list of dictionaries representing users, possibly with
duplicates by `user_id`. Remove duplicates while preserving the order
of first occurrence. Keep the first occurrence of each `user_id`.

Example:
users = [
    {"user_id": 1, "name": "Alice"},
    {"user_id": 2, "name": "Bob"},
    {"user_id": 1, "name": "Alice Smith"},
    {"user_id": 3, "name": "Charlie"},
    {"user_id": 2, "name": "Bob Jr"},
]

Expected:
[
    {"user_id": 1, "name": "Alice"},
    {"user_id": 2, "name": "Bob"},
    {"user_id": 3, "name": "Charlie"},
]
"""
def dedupe_users(users):
    seen = set()
    result=[]
    for user in users:
        uid = user.get("user_id")
        if uid not in seen:
            seen.add(uid)
            result.append(user)
    return result

if __name__ == "__main__":
    users = [
        {"user_id": 1, "name": "Alice"},
        {"user_id": 2, "name": "Bob"},
        {"user_id": 1, "name": "Alice Smith"},
        {"user_id": 3, "name": "Charlie"},
        {"user_id": 2, "name": "Bob Jr"},
    ]
    print(dedupe_users(users))


