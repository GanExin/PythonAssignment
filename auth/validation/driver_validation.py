from PythonAssignment.database import read_users


def validate_driver_email(email):
    email_format_valid = False
    email_unique = False

    if '@' in email and email.count('@') == 1:
        username, domain = email.split('@')
        if '.' in domain:
            email_format_valid = True
        else:
            print("Invalid email format! Please include a '.' in your domain")
    else:
        print("Invalid email format! Please include a '@' in your email")

    user_db = read_users()
    if email not in user_db:
        email_unique = True
    else:
        print("Email already exists in database, please try another email.")

    if email_format_valid and email_unique:
        return True

    return False

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