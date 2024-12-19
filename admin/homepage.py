from PythonAssignment.admin.vehicle_management_and_maintenance import manage_vehicle_and_maintenance
from PythonAssignment.driver_management import manage_driver
from PythonAssignment.admin.manage_fuel_and_consumption import fuel_management_and_vehicle_consumption


def admin_homepage(session):
    print("Admin homepage")
    while True:
            user_choice = int(input(
                "[1] Manage Vehicle and Maintenance \n[2] Manage Driver \n[3] Fuel Management and Vehicle consumption \n[4] View Reports \n[5] Exit \nSelect the following options: "))

            if user_choice == 1:
                manage_vehicle_and_maintenance(session)
            elif user_choice == 2:
                manage_driver(session)
            elif user_choice == 3:
                fuel_management_and_vehicle_consumption(session)
            elif user_choice == 4:
                pass #view_reports(session)
            elif user_choice == 5:
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
                continue
