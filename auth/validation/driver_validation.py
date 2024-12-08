from PythonAssignment.database import read_users

def validate_email(email):
    if '@' not in email and not email.count('@') == 1: #ensure '@' in email and not entered more than once
        print("Invalid email format! Please include a '@' in your email")
        return False
    username, domain = email.split('@')
    if '.' not in domain: #ensure email has'.com'
        print("Invalid email format! Please include a '.' in your domain")
        return False
    if '|' in email: #ensure delimiter is not disturbed
        print("Email cannot contain '|'")
        return False
    existing_users = read_users()
    for user in existing_users:
        existing_email = user[0]
        if email == existing_email: #find if email exist
            print("Email already exists in database_driver, please try another email.")
            return False

    return True


def validate_password(password):
    if len(password) < 3:
        print("Password must be longer than 3 characters")
        return False
    if not any(char.isupper() for char in password):
        print("Password must contain at least 1 capital letter")
        return False
    if '|' in password: #ensure delimiter is not disturbed
        print("Password cannot contain '|'")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least 1 number")
        return False

    return True


def validate_first_name(first_name):
    if not any(char.isalpha() for char in first_name):
        print("First name must contain letters")
        return False
    if not first_name[0].isupper():
        print("First name must start with Capital letter")
        return False
    if any(char.isdigit() for char in first_name):
        print("First name must not contain any numbers")
        return False
    if '|' in first_name: #ensure delimiter is not disturbed
        print("First name must not contain '|'")
        return False

    return True


def validate_last_name(last_name):
    if not any(char.isalpha() for char in last_name):
        print("Last name must contain letters")
        return False
    if not last_name[0].isupper():
        print("Last name must start with Capital letter")
        return False
    if any(char.isdigit() for char in last_name):
        print("last name must not contain any numbers")
        return False
    if '|' in last_name: #ensure delimiter is not disturbed
        print("Last name must not contain '|'")
        return False

    return True


def validate_phone_number(phone_number):
    if not all (char.isdigit() for char in phone_number):
        print("Phone number should only contain numbers")
        return False
    if '|' in phone_number: #ensure delimiter is not disturbed
        print("Phone number must not contain '|'")
        return False

    return True


def validate_address(address):
    if not any (char.isalpha() for char in address):
        print("Address should contain letters")
        return False
    if '|' in address: #ensure delimiter is not disturbed
        print("Address should not contain '|'")
        return False

    return True


def validate_driver_availability_status(availability_status):
    if availability_status not in ['available', 'unavailable']:
        print("Please enter either 'available' or 'unavailable': ")
        return False

    return True


def validate_driver_license(driver_license):
    if not any (char.isdigit() for char in driver_license):
        print("Your driver license should contain numbers")
        return False
    if '|' in driver_license: #ensure delimiter is not disturbed
        print("Driver license should not contain '|'")
        return False

    return True


def validate_driver_health_report(health_report):
    if health_report not in ['1', '2']:
        print("Please select a number: [1]Fit to drive, [2]Not fit to drive")
        return False
    return True

#return value based on input number
def get_health_report_value(health_report):
    if health_report == '1':
        return "fit to drive"
    if health_report == '2':
        return "not fit to drive"


def validate_driver_family_dependencies(family_dependencies):
    if not any (char.isdigit() for char in family_dependencies):
        print("Please enter only numbers")
        return False
    if ' | ' in family_dependencies: #ensure delimiter is not disturbed
        print("Input cannot contain "|" ")
        return False
    return True