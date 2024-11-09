from PythonAssignment.admin.homepage import admin_homepage
from PythonAssignment.driver.homepage import driver_homepage
from PythonAssignment.customer.homepage import customer_homepage
from PythonAssignment.database import read_users


def login():
    user_db = read_users()
    email = str(input("Please enter email: "))
    password = input("Please enter password: ")
    if email in user_db and user_db[email]['password'] == password:
        db = user_db[email]
        role = db['role']
        session = {
            "email": email,
            "role": role,
        }
        if role == 'customer':
            customer_homepage(session)
        elif role == 'driver':
            driver_homepage(session)
        elif role == 'admin':
            admin_homepage(session)
        else:
            print("Invalid role.")
    else:
        print("Login Failed")