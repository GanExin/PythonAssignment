from PythonAssignment.admin.driver_management import view_comment_for_drivers
from PythonAssignment.database import read_driver_details, read_users
from PythonAssignment.driver.delivery_details import view_driver_orders, delivery_details
from PythonAssignment.driver.parcel_and_order_details import update_parcel_status
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
                       "\n[3] View available jobs/parcels"
                       "\n[4] View/update delivery details"
                       "\n[5] View all comments by admins"
                       "\n[6] Exit: ")
        if choice == "1":
            update_password(session)
        if choice == "2":
            update_profile(session)
        if choice == "3":
            update_parcel_status(session)
        if choice == "4":
            delivery_details(session)
        if choice == "5":
            view_comment_for_drivers(session)
        if choice == "6":
            break
