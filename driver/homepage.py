from PythonAssignment.admin.driver_management import view_comment_for_drivers
from PythonAssignment.database import read_driver_details, read_users, update_parcel_details
from PythonAssignment.driver.delivery_details import view_driver_orders, delivery_details
from PythonAssignment.driver.parcel_and_order_details import update_parcel_driver
from PythonAssignment.driver.manage_driver_profile import update_password, update_profile
from PythonAssignment.driver.update_booked_parcel import update_booked_parcel_details
from PythonAssignment.driver.view_vehicle import view_assign_vehicle


#homepage for drivers
def driver_homepage(session):
    profile = read_driver_details(session[0])
    users = read_users()

    print("Welcome back! " + profile[1] + "!")

    while True:
        choice = input("\nWhat would you like to do?(Please select number) "
                       "\n[1] update password "
                       "\n[2] update driver profile "
                       "\n[3] View/book available parcels"
                       "\n[4] Update booked parcel details"
                       "\n[5] View/update delivery details"
                       "\n[6] View all comments by admins"
                       "\n[7] View assigned vehicle"
                       "\n[8] Exit: ")
        if choice == "1":
            update_password(session)
        elif choice == "2":
            update_profile(session)
        elif choice == "3":
            update_parcel_driver(session)
        elif choice == "4":
            update_booked_parcel_details(session)
        elif choice == "5":
            delivery_details(session)
        elif choice == "6":
            view_comment_for_drivers(session)
        elif choice == "7":
            view_assign_vehicle(session)
        elif choice == "8":
            break
