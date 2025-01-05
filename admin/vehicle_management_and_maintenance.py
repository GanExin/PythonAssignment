
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
        with open("./database_admin/vehicle_data.txt", "r") as file:
            lines = file.readlines()

        # Check if there are any existing vehicles, if yes then get the last vehicle id and +1
        if lines:
            last_line = lines[-1]
            last_vehicle_id = last_line.strip().split(" | ")[0]
            next_vehicle_id = str(int(last_vehicle_id) + 1) #get the last vehicle id +1 to generate next vehicle id
        else:
            next_vehicle_id = "1" #if there are no vehicles, just start with 1

        print(f"Assigned Vehicle ID: {next_vehicle_id}")

        vehicle_model = input("Enter Vehicle Model (e.g., Truck, Van, Specialized Carrier): ").strip()

        def valid_date(date_text): #function to validate date format
            if len(date_text) != 10: #length needed to be 10
                return False
            year, month, day = date_text.split('-')
            #ensure year, month, day in the correct length
            return len(year) == 4 and year.isdigit() and len(month) == 2 and month.isdigit() and len(
                day) == 2 and day.isdigit()

        # Loop until the valid date is entered
        last_inspection = ""
        while not valid_date(last_inspection):
            last_inspection = input("Enter Last Inspection Date (YYYY-MM-DD): ").strip()
            if not valid_date(last_inspection):
                print("Error: Invalid Last Inspection Date format. Please use YYYY-MM-DD.")

        next_inspection = ""
        while not valid_date(next_inspection):
            next_inspection = input("Enter Next Inspection Date (YYYY-MM-DD): ").strip()
            if not valid_date(next_inspection):
                print("Error: Invalid Next Inspection Date format. Please use YYYY-MM-DD.")

        performance = input("Enter Vehicle Performance (e.g., Good, Excellent, Poor): ").strip()

        def valid_maintenance(maintenance_text): # Function to validate the maintenance history format
            if maintenance_text.lower() == "no maintenance record" or not maintenance_text.strip():
                return True # If no record or empty, it's valid
            entries = maintenance_text.split("|")
            for entry in entries:
                if ":" not in entry:
                    return False # Ensure each entry has the format date:task
                date, task = entry.split(":", 1)
                if not valid_date(date) or not task.strip():
                    return False  # Check if date and task are valid
            return True

       # Loop until a valid entry is made
        maintenance_history = ""
        while True:
            maintenance_history = input(
                "Enter Maintenance History (e.g., 2024-12-15: Tire Rotation|2024-12-31: Oil Change or type 'no maintenance record'): ").strip()
            if valid_maintenance(maintenance_history):
                break #Exit loop after valid
            print("Error: Invalid Maintenance History format. Please use YYYY-MM-DD:Task|YYYY-MM-DD:Task.")

        if not maintenance_history.strip() or maintenance_history.lower() == "no maintenance record":
            maintenance_history = "No maintenance record"

        cargo_suitability = input("Enter Suitable Cargo (e.g., Small Cargo, Heavy Cargo): ").strip()

        new_vehicle_data = (
            f"{next_vehicle_id} | {vehicle_model} | {last_inspection} | {next_inspection} | {performance} | "
            f"{maintenance_history} | Suitable for {cargo_suitability}\n")

        with open("./database_admin/vehicle_data.txt", "a") as file:
            file.write(new_vehicle_data)

        print("\nNew vehicle added successfully!")
        print(f"Details: {new_vehicle_data}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def view_vehicle_detail(session):
    print("---------------View Vehicle Detail---------------")
    vehicle_id = input("Please enter the vehicle ID:")

    try:
        with open("./database_admin/vehicle_data.txt", "r") as file:
            found = False  # Flag to track if the vehicle was found
            for line in file:

                vehicle_data = line.strip().split(" | ")

                # Check if the vehicle ID matches the one entered by the user
                if vehicle_data[0] == vehicle_id:
                    found = True  # Set found flag to True

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

    # Helper function to ensure valid date input (YYYY-MM-DD format)
    def get_valid_date(prompt):
        while True:
            date_text = input(prompt).strip()
            if len(date_text) == 10 and date_text.count('-') == 2:
                parts = date_text.split('-')
                year, month, day = parts
                # Check if year, month, day are digits and in the correct length
                if year.isdigit() and len(year) == 4 and \
                        month.isdigit() and len(month) == 2 and \
                        day.isdigit() and len(day) == 2:
                    return date_text
            print("Error: Invalid date format. Please enter the date in YYYY-MM-DD format.")

    try:
        with open("./database_admin/vehicle_data.txt", "r") as file:
            lines = file.readlines()

        found = False
        for i, line in enumerate(lines):
            vehicle_detail = line.strip().split(" | ")

            if vehicle_detail[0] == vehicle_id:
                found = True

                current_inspection_date = vehicle_detail[3]  # Retrieve current inspection date
                print(f"Current inspection date: {current_inspection_date}")

                # Store the current inspection date as the last inspection date
                last_inspection_date = current_inspection_date

                # Prompt the user to enter a new inspection date
                new_inspection_date = get_valid_date("Please enter the new inspection date (YYYY-MM-DD): ")

                # Update the vehicle details with the new and old inspection dates
                vehicle_detail[2] = last_inspection_date
                vehicle_detail[3] = new_inspection_date

                # Join the updated vehicle details into a single line
                updated_line = " | ".join(vehicle_detail) + "\n"
                lines[i] = updated_line  # Replace the old line with the updated one
                break  # Exit the loop after updating the vehicle

        if found:
            with open("./database_admin/vehicle_data.txt", "w") as file:
                file.writelines(lines)

            print(f"Inspection date for Vehicle ID {vehicle_id} was successfully updated to {new_inspection_date}.")
            print(f"Last inspection date for Vehicle ID {vehicle_id} was updated to {last_inspection_date}.")
        else:
            print("Vehicle not found. Please check the ID and try again.")

    except FileNotFoundError:
        print("No vehicle data found. Please ensure the vehicle data file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def assign_vehicle_to_driver(session):
    print("---------------Assign Vehicle to Driver---------------")

    driver_email = input("Enter the Driver Email: ").strip()

    try:
        driver_found = False
        with open("./database_driver/driver_profile.txt", "r") as driver_file:
            driver_lines = driver_file.readlines()
            for driver_line in driver_lines:
                driver_detail = driver_line.strip().split(" | ")
                if driver_detail[0].strip().lower() == driver_email.lower(): # Check if the email matches the input
                    driver_found = True
                    break

        if not driver_found:
            print(f"Driver with email {driver_email} not found.")
            return

        vehicle_id = input("Enter the Vehicle ID: ").strip()

        vehicle_exists = False
        vehicle_performance = None
        with open("./database_admin/vehicle_data.txt", "r") as vehicle_file:
            vehicle_lines = vehicle_file.readlines()
            for vehicle_line in vehicle_lines:
                vehicle_detail = vehicle_line.strip().split(' | ')
                if vehicle_detail[0] == vehicle_id: # Check if the vehicle ID matches the input
                    vehicle_exists = True
                    vehicle_performance = vehicle_detail[4] if len(vehicle_detail) > 4 else None
                    break

        # If the vehicle doesn't exist, print a message and exit
        if not vehicle_exists:
            print(f"Vehicle ID {vehicle_id} does not exist in the vehicle database.")
            return

        # If the vehicle's performance is poor, print a message and exit
        if vehicle_performance and vehicle_performance.lower() == "poor":
            print(f"Vehicle ID {vehicle_id} has poor performance and cannot be assigned.")
            return

        # Check if the vehicle is already assigned to a driver
        for driver_line in driver_lines:
            driver_detail = driver_line.strip().split(" | ")
            assigned_vehicle_id = driver_detail[9].strip().lower() if len(driver_detail) > 9 else "none"
            if assigned_vehicle_id == vehicle_id.lower():
                print(f"Vehicle ID {vehicle_id} is already assigned to driver {driver_detail[0]}.")
                return

        # Assign the vehicle to the driver
        for i, driver_line in enumerate(driver_lines):
            driver_detail = driver_line.strip().split(" | ")
            if driver_detail[0].strip().lower() == driver_email.lower():
                # Check the driver's health status before assigning
                health_report = driver_detail[7].strip().lower()
                if health_report == "not fit to drive":
                    print(f"Driver {driver_email} is not fit to drive.")
                    return

                # If the driver already has a vehicle, ask if they want to reassign it
                if driver_detail[9].strip().lower() != "none":
                    current_vehicle_id = driver_detail[9].strip()
                    print(f"Driver {driver_email} is already assigned to Vehicle ID {current_vehicle_id}.")
                    reassign = input("Do you want to reassign a new vehicle? (yes/no): ").strip().lower()
                    if reassign != "yes":
                        return

                driver_lines[i] = f"{driver_detail[0]} | {driver_detail[1]} | {driver_detail[2]} | {driver_detail[3]} | {driver_detail[4]} | {driver_detail[5]} | {driver_detail[6]} | {driver_detail[7]} | {driver_detail[8]} | {vehicle_id}\n"
                break

        with open("./database_driver/driver_profile.txt", "w") as driver_file:
            driver_file.writelines(driver_lines)

        print(f"\nSuccessfully assigned Vehicle ID {vehicle_id} to Driver with email {driver_email}.")

    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def check_maintenance_alerts(session):
    # function to validate date input
    def get_valid_date(prompt):
        while True:
            date_text = input(prompt).strip()
            if len(date_text) == 10 and date_text.count('-') == 2:
                parts = date_text.split('-')
                year, month, day = parts
                # Validate year, month, and day components of the date
                if year.isdigit() and len(year) == 4 and \
                   month.isdigit() and len(month) == 2 and \
                   day.isdigit() and len(day) == 2:
                    return date_text
            print("Error: Invalid date format. Please enter the date in YYYY-MM-DD format.")

    # Prompt the user for the date to check maintenance alerts
    user_input_date = get_valid_date("Enter the date to check maintenance alerts (YYYY-MM-DD): ")

    try:
        with open("./database_admin/vehicle_data.txt", 'r') as file:
            lines = file.readlines()

        # List to hold all the maintenance alerts
        alerts = []
        for line in lines:
            vehicle_detail = line.strip().split(' | ')

            # Ensure the line contains the expected number of elements (at least 4)
            if len(vehicle_detail) >= 4:
                # Extract the next inspection date from the vehicle data
                next_inspection_date = vehicle_detail[3]

                # Compare the next inspection date with the user input date
                if next_inspection_date <= user_input_date:
                    # If the inspection is due, add a maintenance alert to the list
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
    print("---------------Update Maintenance Record---------------")
    vehicle_id = input("Enter the Vehicle ID: ").strip()

    try:
        with open("./database_admin/vehicle_data.txt", 'r') as file:
            lines = file.readlines()

        # Check if the provided vehicle ID exists in the vehicle data
        vehicle_exists = any(line.strip().split(' | ')[0] == vehicle_id for line in lines)

        if not vehicle_exists:
            print(f"Vehicle ID {vehicle_id} does not exist in the vehicle database.")
            return

        #function to validate the date format
        def get_valid_date(prompt):
            while True:
                date_text = input(prompt).strip()
                parts = date_text.split('-')
                if len(parts) == 3 and all(part.isdigit() for part in parts):
                    year, month, day = parts
                    if len(year) == 4 and len(month) == 2 and len(day) == 2:
                        return date_text
                print("Error: Invalid date format. Please enter the date in YYYY-MM-DD format.")

        # Prompt the user for the new maintenance date and action
        new_maintenance_date = get_valid_date("Enter the new maintenance date (YYYY-MM-DD): ")
        new_maintenance_action = input("Enter the new maintenance action (e.g., 'Oil Change', 'Tire Rotation', etc.): ").strip()

        for i, line in enumerate(lines):
            vehicle_detail = line.strip().split(' | ')

            if vehicle_detail[0] == vehicle_id:
                # Get the current maintenance history or create an empty list
                maintenance_history = vehicle_detail[5].split('|') if len(vehicle_detail) > 5 else []

                # Check if there's already a maintenance record for the specified date
                for j, record in enumerate(maintenance_history):
                    record_date, _ = record.split(':')
                    if record_date == new_maintenance_date:
                        # Update the existing record if the date matches
                        maintenance_history[j] = f"{new_maintenance_date}:{new_maintenance_action}"
                        break
                else:
                    # If the date does not match, append a new record
                    maintenance_history.append(f"{new_maintenance_date}:{new_maintenance_action}")

                # Update the vehicle details with the new maintenance history
                vehicle_detail[5] = "|".join(maintenance_history)
                lines[i] = " | ".join(vehicle_detail) + "\n"
                break

        with open("./database_admin/vehicle_data.txt", 'w') as file:
            file.writelines(lines)

        print(f"Maintenance record for Vehicle ID {vehicle_id} updated with action: {new_maintenance_action} on {new_maintenance_date}.")

    except FileNotFoundError:
        print("Vehicle data file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")










