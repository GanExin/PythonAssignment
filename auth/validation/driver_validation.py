from PythonAssignment.database import read_users


def validate_driver_email(email):
    username, domain = email.split('@')
    user_db = read_users()
    if '@' not in email and not email.count('@') == 1:
        print("Invalid email format! Please include a '@' in your email")
        return False
    if '.' not in domain:
        print("Invalid email format! Please include a '.' in your domain")
        return False
    if '|' in email:
        print("Email cannot contain '|'")
        return False
    if email in user_db:
        print("Email already exists in database, please try another email.")
        return False

    return True


def validate_driver_password(password):
    if len(password) < 3:
        print("Password must be longer than 3 characters")
        return False
    if not any(char.isupper() for char in password):
        print("Password must contain at least 1 capital letter")
        return False
    if '|' in password:
        print("Password cannot contain '|'")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least 1 number")
        return False

    return True