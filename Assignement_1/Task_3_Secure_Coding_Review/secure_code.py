# Task 3: Secure Code Example
# Fix: Using Environment Variables
import os

def connect_to_database():
    # SAFE: We pull the password from the system, not the code!
    db_password = os.getenv("DB_PASSWORD")
    print("Connecting securely...")

connect_to_database()