#validate date
def validate_date(date):
    if len(date) != 10 or date[2] != '/' or date[5] != '/': #ensure '/' between date,month,year
        print("Invalid date format. Please use 'dd/mm/yyyy'.")
        return False
    if any(char.isalpha() for char in date): #ensure no letters are entered
        print("Date cannot contain letters")
        return False

    day, month, year = date[:2], date[3:5], date[6:] #clarify which is dd,mm,yyyy

    if not (day.isdigit() and month.isdigit() and year.isdigit()): #ensure dd,mm,yyyy are numbers
        return "Invalid date format. Day, month, and year must be numbers."

    day, month, year = int(day), int(month), int(year) #convert input to intergers
    if month < 1 or month > 12: #ensure month is valid
        print("Invalid month. It must be between 1 and 12.")
        return False
    if day < 1 or day > 31: #ensure day is valid
        print("Invalid day. It must be between 1 and 31.")
        return False
    return True