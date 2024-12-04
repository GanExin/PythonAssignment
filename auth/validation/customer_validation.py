from PythonAssignment.database import read_users


def validate_customer_email(email):
    if '@' not in email and not email.count('@') == 1:
        print("Invalid email format! Please include a '@' in your email")
        return False
    username, domain = email.split('@')
    if '.' not in domain:
        print("Invalid email format! Please include a '.' in your domain")
        return False
    if email == "" :
        print("Email must not be empty")
        return False
    if '|' in email:
        print("Email cannot contain '|'")
        return False
    existing_users = read_users()
    for user in existing_users:
        existing_email = user[0]
        if email == existing_email:
            print("Email already exists in database, please try another email.")
            return False

    return True


def validate_customer_password(password):
    if password == "" :
        print("Password must not be empty")
        return False
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

def validate_customer_fullname(fullname):
    if fullname == "":
        print("Full name must not be empty")
        return False
    if not any(char.isalpha() for char in fullname):
        print("Full name must contain letters")
        return False
    if not fullname[0].isupper():
        print("Full name must be capitalized")
        return False
    if any(char.isdigit() for char in fullname):
        print("Full name must not contain any numbers")
        return False
    if '|' in fullname:
        print("Full name must not contain '|'")
        return False

    return True

def validate_customer_phone_number(phone_number):
    if not all (char.isdigit() for char in phone_number):
        print("Phone number should only contain numbers")
        return False
    if phone_number == "":
        print("Phone number must not be empty")
        return False
    if '|' in phone_number:
        print("Phone number must not contain '|'")
        return False

    return True


def validate_customer_address(address):
    if not any (char.isalpha() for char in address):
        print("Address should contain letters")
        return False
    if address == "":
        print("Address must not be empty")
        return False
    if '|' in address:
        print("Address should not contain '|'")
        return False

    return True