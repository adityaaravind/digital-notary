import json
import hashlib
import os

USER_DB = "users.json"

def load_users():
    if not os.path.exists(USER_DB):
        with open(USER_DB, "w") as f:
            json.dump({}, f)
    with open(USER_DB, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=4)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = hashlib.sha256(password.encode()).hexdigest()
    save_users(users)
    return True

def authenticate_user(username, password):
    users = load_users()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return users.get(username) == hashed