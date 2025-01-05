from PythonAssignment.database import read_users, read_driver_details, display_vehicle_data


def view_assign_vehicle(session):
    users = read_users()
    current_user = session[0] #check if current user match email aka session[0]

    drivers = read_driver_details(current_user)
    assigned_vehicle = drivers[9] #driver [9] should be the vehicle id (either a vehicle ID or "None")
    for user in users:
        db_email = user[0]
        if current_user == db_email:
            print("\n---------------------View Assigned Vehicle---------------------\n")

            if assigned_vehicle and assigned_vehicle != "None": #if not empty and is not "None" print
                vehicle_details = display_vehicle_data(assigned_vehicle) #display vehicle details by matching ID
                print(vehicle_details)
            else:
                print("No vehicle assigned yet.")
            return
