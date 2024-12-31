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
            print("Email already exists in database, please try another email.")
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


def validate_number(number):
    if not all (char.isdigit() for char in number):
        print("Input should only contain numbers")
        return False
    if '|' in number: #ensure delimiter is not disturbed
        print("Input must not contain '|'")
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


def validate_route_chosen(route):
    if route not in ['1','2']:
        print("Please select a number")
        return False
    if ' | ' in route: #ensure delimiter is not disturbed
        print("Input cannot contain "|" ")
        return False
    return True


def validate_date_time(date_time):
    #Ensure format to separate date and time is correct
    if ' | ' in date_time:  # ensure delimiter is not disturbed
        print("Input cannot contain " | " ")
        return False
    if not date_time or ";" not in date_time:
        print("Invalid format. Use 'DD/MM/YYYY; HH:MM'.")
        return False

    try:
        # Split into date and time
        date_part, time_part = date_time.split("; ")

        # Validate date part (DD/MM/YYYY)
        day, month, year = map(int, date_part.split("/"))
        if not (1 <= day <= 31):
            print("Invalid day. Day should be between 1 and 31.")
            return False
        if not (1 <= month <= 12):
            print("Invalid month. Month should be between 1 and 12.")
            return False
        if len(str(year)) != 4: #validate 4-digit year length
            print("Invalid year. Year should be a 4-digit number.")
            return False

        # Validate time part (HH:MM)
        hour, minute = map(int, time_part.split(":"))
        if not (00 <= hour <= 23):
            print("Invalid hour. Hour should be between 00 and 23.")
            return False
        if not (00 <= minute <= 59):
            print("Invalid minute. Minute should be between 00 and 59.")
            return False

        return True
    except ValueError:
        print("Invalid format. Use 'DD/MM/YYYY; HH:MM'.")
        return False


def validate_float_with_two_decimals(f_number):
    if ' | ' in f_number: #ensure delimiter is not disturbed
        print("Input cannot contain "|" ")
        return False

    try:
        #check if it can be converted to a float
        float_number = float(f_number)

        #check if it matches the two-decimal format
        parts = f_number.split(".")
        if len(parts) == 2 and len(parts[1]) == 2:
            return True
        else:
            print("Input must be a number with exactly two decimal places.")
            return False
    except ValueError:
        print("Input must be a valid floating-point number.")
        return False

def validate_yes_or_no(y_n):
    if y_n not in ['y','n']:
        print("Please enter either (y/n)")
        return False
    if ' | ' in y_n: #ensure delimiter is not disturbed
        print("Input cannot contain "|" ")
        return False
    return True
