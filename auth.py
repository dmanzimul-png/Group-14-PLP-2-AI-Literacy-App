"""
auth.py — User Authentication
Handles user registration and login using the local SQLite database.
"""

import hashlib
from Database import get_connection

VALID_AGE_GROUPS = ["Under 13", "13-17", "18-25", "26+"]

def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
