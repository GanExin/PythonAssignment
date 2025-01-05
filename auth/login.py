from PythonAssignment.admin.homepage import admin_homepage
from PythonAssignment.customer.homepage import customer_homepage
from PythonAssignment.database import read_users
from PythonAssignment.driver.homepage import driver_homepage


def login():
    users = read_users()
    email_input = str(input("Please enter email: "))
    password_input = input("Please enter password: ")
    for user in users:
        email = user[0] #email = the 1st index of "user"
        password = user[1] #password = the 2nd index of "user"
        if email_input == email and password_input == password: #ensure password and email input match database records
            role = user[2] #find role of user
            session = [email, role] #store matching email and role as "session"
            if role == 'customer':
                customer_homepage(session)
                return True
            if role == 'driver':
                driver_homepage(session)
                return True
            if role == 'admin':
                admin_homepage(session)
                return True
    return False
    #return false if email and password does not match