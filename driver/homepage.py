from PythonAssignment.database import read_driver_details


def driver_homepage(session):
    email = session['email']
    driver_db = read_driver_details(email)
    first_name = driver_db['first_name']

    print("Welcome back! " + first_name + "!")