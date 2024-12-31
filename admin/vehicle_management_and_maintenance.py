
from PythonAssignment.database import display_vehicle_data

def vehicle_management_and_maintenance(session):
    print("------------------Vehicle Management and Maintenance------------------")
    # User selects a feature from the menu
    while True:
        choice = input("[1] Add New Vehicle \n[2] View Vehicle Detail"
                       "\n[3] Schedule Inspection \n[4] Assign Vehicle to Driver"
                       "\n[5] Check Maintenance Alerts \n[6] Update Maintenance Record "
                       "\n[7] Exit"
                       "\nPlease choose a feature (1/2/3/4/5/6/7): ")

        if choice == "1":
            add_new_vehicle(session)
        elif choice == '2':
            view_vehicle_detail(session)
        elif choice == '3':
            schedule_inspection(session)
        elif choice == '4':
            assign_vehicle_to_driver(session)
        elif choice == '5':
            check_maintenance_alerts(session)
        elif choice == '6':
            update_maintenance_record(session)
        elif choice == '7':
            print("Exiting Vehicle Management and Maintenance.")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

def add_new_vehicle(session):
    print("---------------Add New Vehicle---------------")

    try:
        vehicle_id = input("Enter Vehicle ID (e.g., 7): ").strip()
        vehicle_model = input("Enter Vehicle Model (e.g., Toyota Corolla): ").strip()
        last_inspection = input("Enter Last Inspection Date (YYYY-MM-DD): ").strip()
        next_inspection = input("Enter Next Inspection Date (YYYY-MM-DD): ").strip()
        performance = input("Enter Vehicle Performance (e.g., Good, Excellent, Poor): ").strip()
        maintenance_history = input("Enter Maintenance History (e.g., 2023-12-01:Oil Change|2023-11-01:Tire Rotation): ").strip()
        cargo_suitability = input("Enter Suitable Cargo (e.g., Small Cargo, Heavy Cargo): ").strip()

        # Validate that none of the fields are empty
        if not (vehicle_id and vehicle_model and last_inspection and next_inspection and performance and maintenance_history and cargo_suitability):
            print("All fields are required. Please fill in all details.")
            return

        new_vehicle_data = (f"{vehicle_id} | {vehicle_model} | {last_inspection} | {next_inspection} | {performance} | "
                            f"{maintenance_history} | Suitable for Cargo: {cargo_suitability}\n")

        # Append the new vehicle data to the file
        with open("./database_admin/vehicle_data.txt", "a") as file:
            file.write(new_vehicle_data)

        print("\nNew vehicle added successfully!")
        print(f"Details: {new_vehicle_data}")

    except FileNotFoundError:
        print("Vehicle data file not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_vehicle_detail(session):
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


def schedule_inspection(session):
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

def assign_vehicle_to_driver(session):
    print("---------------Assign Vehicle to Driver---------------")

    driver_email = input("Enter the Driver Email: ").strip()
    vehicle_id = input("Enter the Vehicle ID: ").strip()

    try:
        with open("./database_admin/driver_vehicle_assigned_data.txt", "r") as driver_file:
            driver_lines = driver_file.readlines()

        driver_found = False
        for i, driver_line in enumerate(driver_lines):
            driver_detail = driver_line.strip().split(" | ")
            if driver_detail[0].strip().lower() == driver_email.lower():
                driver_found = True
                if driver_detail[4].strip().lower() != "none":
                    print(f"Driver with email {driver_email} is already assigned to Vehicle ID {driver_detail[4].strip()}.")
                    return

                driver_lines[i] = f"{driver_detail[0]} | {driver_detail[1]} | {driver_detail[2]} | {driver_detail[3]} | {vehicle_id}\n"
                break

        if not driver_found:
            print(f"Driver with email {driver_email} not found.")
            return

        with open("./database_admin/driver_vehicle_assigned_data.txt", "w") as driver_file:
            driver_file.writelines(driver_lines)

        print(f"Successfully assigned Vehicle ID {vehicle_id} to Driver with email {driver_email}.")

    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def check_maintenance_alerts(session):
    user_input_date = input("Enter the date to check maintenance alerts (YYYY-MM-DD): ")

    try:
        with open("./database_admin/vehicle_data.txt", 'r') as file:
            lines = file.readlines()

        alerts = []
        for line in lines:
            vehicle_detail = line.strip().split(' | ')

            if len(vehicle_detail) >= 4:  # Check if the line has enough data
                next_inspection_date = vehicle_detail[3]

                # Check if the next inspection date is before or on the provided date
                if next_inspection_date <= user_input_date:
                    alerts.append(
                        f"Vehicle ID: {vehicle_detail[0]} (Model: {vehicle_detail[1]}) "
                        f"needs maintenance inspection by {next_inspection_date}."
                    )

        if alerts:
            print("\nMaintenance Alerts:")
            for alert in alerts:
                print(alert)
        else:
            print("No maintenance inspections due on or before the provided date.")

    except FileNotFoundError:
        print("Vehicle data file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def update_maintenance_record(session):
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









