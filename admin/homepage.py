from PythonAssignment.admin.driver_management import driver_management
from PythonAssignment.admin.manage_fuel_and_consumption import manage_fuel_and_consumption
from PythonAssignment.admin.vehicle_management_and_maintenance import vehicle_management_and_maintenance


def admin_homepage(session):
    print("Admin homepage")
    while True:
            user_choice = int(input(
                "[1] Manage Vehicle and Maintenance \n[2] Manage Driver \n[3] Fuel Management and Vehicle consumption \n[4] View Reports \n[5] Exit \nSelect the following options: "))

            if user_choice == 1:
                vehicle_management_and_maintenance(session)
            elif user_choice == 2:
                driver_management(session)
            elif user_choice == 3:
                manage_fuel_and_consumption(session)
            elif user_choice == 4:
                pass #view_reports(session)
            elif user_choice == 5:
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
                continue
