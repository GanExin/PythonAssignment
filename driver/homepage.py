from PythonAssignment.database import read_driver_details, read_users
from PythonAssignment.driver.parcel_and_order_details import prompt_for_order_id, update_parcel_status
from PythonAssignment.driver.manage_driver_profile import update_password, update_profile

#homepage for drivers
def driver_homepage(session):
    profile = read_driver_details(session[0])
    users = read_users()

    print("Welcome back! " + profile[1] + "!")

    while True:
        choice = input("\nWhat would you like to do?(Please select number) "
                       "\n[1] update password "
                       "\n[2] update driver profile "
                       "\n[3] View Order details "
                       "\n[4] update Order status"
                       "\n[5] Exit: ")
        if choice == "1":
            update_password(session)
        if choice == "2":
            update_profile(session)
        if choice == "3":
            prompt_for_order_id(session)
        if choice == "4":
            update_parcel_status(session)
        if choice == "5":
            break
