from PythonAssignment.admin.vehicle_management_and_maintenance import view_vehicle_detail
from PythonAssignment.database import read_users, read_driver_details, display_driver_details, display_vehicle_data


def view_assign_vehicle(session):
    users = read_users()
    current_user = session[0] #check if current user match email aka session[0]

    drivers = read_driver_details(current_user)
    assigned_vehicle = drivers[9]
    for user in users:
        db_email = user[0]
        if current_user == db_email:
            print("\n---------------------View Assigned Vehicle---------------------\n")

            if assigned_vehicle and assigned_vehicle != "None":
                vehicle_details = display_vehicle_data(assigned_vehicle)
                print(vehicle_details)
            else:
                print("No vehicle assigned yet.")
            return
