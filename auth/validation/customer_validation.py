from PythonAssignment.database import read_users


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
