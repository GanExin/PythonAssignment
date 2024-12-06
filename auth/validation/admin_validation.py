def validate_date_of_birth(date_of_birth):
    if len(date_of_birth) != 10 or date_of_birth[2] != '/' or date_of_birth[5] != '/':
        print("Invalid date format. Please use 'dd/mm/yyyy'.")
        return False
    if any(char.isalpha() for char in date_of_birth):
        print("Date of birth cannot contain letters")
        return False

    day, month, year = date_of_birth[:2], date_of_birth[3:5], date_of_birth[6:]

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return "Invalid date format. Day, month, and year must be numbers."

    day, month, year = int(day), int(month), int(year)
    if month < 1 or month > 12:
        print("Invalid month. It must be between 1 and 12.")
        return False
    if day < 1 or day > 31:
        print("Invalid day. It must be between 1 and 31.")
        return False
    return True