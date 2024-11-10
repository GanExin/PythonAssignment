from PythonAssignment.admin.homepage import admin_homepage
from PythonAssignment.driver.homepage import driver_homepage
from PythonAssignment.customer.homepage import customer_homepage
from PythonAssignment.database import read_users

def login():
    users = read_users()
    email_input = str(input("Please enter email: "))
    password_input = input("Please enter password: ")
    for user in users:
        email = user[0]
        password = user[1]
        if email_input == email and password_input == password:
            role = user[2]
            session = [email, role]
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