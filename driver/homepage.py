from PythonAssignment.database import read_driver_details


def driver_homepage(session):
    profile = read_driver_details(session[0])

    print("Welcome back! " + profile[1] + "!")
