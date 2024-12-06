from PythonAssignment.database import read_driver_details, read_users
from PythonAssignment.driver.manage_driver_profile import update_password, update_profile


def driver_homepage(session):
    profile = read_driver_details(session[0])
    users = read_users()

    print("Welcome back! " + profile[1] + "!")

    while True:
        choice = input("What would you like to do?(Please select number) \n[1] update password \n[2] update driver profile \n[3] Exit: ")
        if choice == "1":
            update_password(session)
        if choice == "2":
            update_profile(session)
        if choice == "3":
            return
        else:
            print("Invalid input")
