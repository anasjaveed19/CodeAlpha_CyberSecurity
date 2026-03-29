# Task 3: Vulnerable Code Example
# Problem: Hardcoded Credentials

def connect_to_database():
    # DANGER: The password is written in plain text!
    db_password = "Admin_Password_2026" 
    print("Connecting with password...")

connect_to_database()