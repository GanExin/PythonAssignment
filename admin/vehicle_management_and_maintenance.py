from PythonAssignment.database import display_vehicle_data

def vehicle_management_and_maintenance(session):
    print("------------------Vehicle Management and Maintenance------------------")
    # User selects a feature from the menu
    while True:
        choice = input("[1] View Vehicle Detail \n[2] Schedule Inspection"
                       "\n[3] Check Maintenance Alerts \n[4] Update Maintenance Record"
                       "\n[5] Exit"
                       "\nPlease choose a feature (1/2/3/4/5): ")
        if choice == '1':
            view_vehicle_detail(session)
        elif choice == '2':
            schedule_inspection(session)
        elif choice == '3':
            check_maintenance_alerts(session)
        elif choice == '4':
            update_maintenance_record(session)
        elif choice == '5':
            print("Exiting Vehicle Management and Maintenance.")
            break
        else:
            print("Invalid input. Please enter a valid choice.")


def view_vehicle_detail():
    print("---------------View Vehicle Detail---------------")
    vehicle_id = input("Please enter the vehicle ID:")

    try:
        with open("./database_admin/vehicle_data.txt", "r") as file:
            found = False
            for line in file:

                vehicle_data = line.strip().split(" | ")
                if vehicle_data[0] == vehicle_id:
                    found = True

                    vehicle_details = display_vehicle_data(vehicle_data)
                    print("\nVehicle Detail:")
                    print(vehicle_details)
                    break
            if not found:
                print("Vehicle not found. Please check the ID and try again.")
    except FileNotFoundError:
        print("No vehicle data found. Please ensure the vehicle data file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def schedule_inspection():
    print("---------------Schedule Vehicle Inspection---------------")
    vehicle_id = input("Please enter the vehicle ID: ")
    new_inspection_date = input("Please enter the new inspection date (YYYY-MM-DD): ")

    try:
        with open("./database_admin/vehicle_data.txt", "r") as file:
            lines = file.readlines()

        found = False
        for i, line in enumerate(lines):
            vehicle_detail = line.strip().split(" | ")

            if vehicle_detail[0] == vehicle_id:
                found = True

                vehicle_detail[3] = new_inspection_date
                updated_line = " | ".join(vehicle_detail) + "\n"
                lines[i] = updated_line
                break

        if found:
            with open("./database_admin/vehicle_data.txt", "w") as file:
                file.writelines(lines)

            print(f"Inspection date for Vehicle ID {vehicle_id} was successfully updated to {new_inspection_date}.")
        else:
            print("Vehicle not found. Please check the ID and try again.")

    except FileNotFoundError:
        print("No vehicle data found. Please ensure the vehicle data file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def check_maintenance_alerts():
    user_input_date = input("Enter the date to check maintenance alerts (YYYY-MM-DD): ")

    try:
        with open("./database_admin/vehicle_data.txt", 'r') as file:
            lines = file.readlines()

        alerts = []
        for line in lines:
            vehicle_detail = line.strip().split(' | ')
            if len(vehicle_detail) > 3:
                next_inspection_date = vehicle_detail[3]
                if next_inspection_date:

                    if next_inspection_date <= user_input_date:
                        alerts.append(
                            f"Vehicle ID: {vehicle_detail[0]} needs maintenance inspection by {next_inspection_date}.")

        if alerts:
            return "\n".join(alerts)
        else:
            return "No maintenance inspections due on or before the provided date."

    except FileNotFoundError:
        return "Vehicle data file not found."
    except Exception as e:
        return f"An error occurred: {e}"

def update_maintenance_record():
    vehicle_id = input("Enter the Vehicle ID: ")
    new_maintenance_date = input("Enter the new maintenance date (YYYY-MM-DD): ")
    new_maintenance_action = input("Enter the new maintenance action (e.g., 'Oil Change', 'Tire Rotation', etc.): ")

    try:
        with open("./database_admin/vehicle_data.txt", 'r') as file:
            lines = file.readlines()

        updated = False
        for i, line in enumerate(lines):
            vehicle_detail = line.strip().split(' | ')

            if vehicle_detail[0] == vehicle_id:
                updated = True

                if len(vehicle_detail) > 5:
                    maintenance_history = vehicle_detail[5].split('|')
                else:
                    maintenance_history = []

                for j, record in enumerate(maintenance_history):
                    record_date, _ = record.split(':')
                    if record_date == new_maintenance_date:
                        maintenance_history[j] = f"{new_maintenance_date}:{new_maintenance_action}"
                        break
                else:
                    maintenance_history.append(f"{new_maintenance_date}:{new_maintenance_action}")

                vehicle_detail[5] = "|".join(maintenance_history)
                lines[i] = " | ".join(vehicle_detail) + "\n"
                break

        if updated:
            with open("./database_admin/vehicle_data.txt", 'w') as file:
                file.writelines(lines)
            print(f"Maintenance record for Vehicle ID {vehicle_id} updated with action: {new_maintenance_action} on {new_maintenance_date}.")
        else:
            print("Vehicle ID not found.")

    except FileNotFoundError:
        print("Vehicle data file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")









