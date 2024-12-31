from PythonAssignment.database import display_fuel_data

def manage_fuel_and_consumption(session):
    print("------------------Manage Fuel and Vehicle Consumption------------------")
    while True:
        choice = input("[1] View Fuel Data \n[2] Update Fuel Data"
                       "\n[3] Track Fuel Consumption \n[4] Check Low Fuel Alert"
                       "\n[5] Exit"
                       "\nPlease choose a feature (1/2/3/4/5): ")
        if choice == '1':
            view_fuel_data(session)
        elif choice == '2':
            update_fuel_data(session)
        elif choice == '3':
            track_fuel_consumption(session)
        elif choice == '4':
            check_low_fuel_alerts(session)
        elif choice == '5':
            print("Exiting Manage Fuel and Vehicle Consumption.")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

def view_fuel_data(session):
    print("---------------View Fuel Data---------------")
    vehicle_id = input("Please enter the vehicle ID:")

    try:
        with open("./database_admin/fuel_data.txt", "r") as file:
            found = False
            for line in file:
                fuel_data = line.strip().split(" | ")
                if fuel_data[0] == vehicle_id:
                    found = True

                    fuel_details = display_fuel_data(fuel_data)
                    print("\nFuel Data:")
                    print(fuel_details)
                    break
            if not found:
                print("Vehicle not found. Please check the ID and try again.")
    except FileNotFoundError:
        print("No fuel data found. Please ensure the fuel data file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def update_fuel_data(session):
    print("---------------Update Vehicle Fuel Data---------------")
    vehicle_id = input("Please enter the vehicle ID to update fuel data: ")

    try:
        with open("./database_admin/fuel_data.txt", 'r') as file:
            lines = file.readlines()

        updated = False
        for i, line in enumerate(lines):
            vehicle_data = line.strip().split(" | ")
            if vehicle_data[0] == vehicle_id:
                updated = True

                current_fuel_level = vehicle_data[2].strip()
                current_mileage = vehicle_data[3].strip()
                current_last_check = vehicle_data[4].strip()
                current_fuel_consumed = vehicle_data[5].strip()

                fuel_level = input(f"Enter new Fuel Level (current: {current_fuel_level}): ")
                mileage = input(f"Enter new Mileage (current: {current_mileage}): ")
                last_fuel_check = input(f"Enter new fuel check (current: {current_last_check}): ")
                fuel_consumed = input(f"Enter new Fuel Consumed (current: {current_fuel_consumed}): ")

                vehicle_data[2] = f"{fuel_level.strip()}%"
                vehicle_data[3] = f"{mileage.strip()} km"
                vehicle_data[4] = f"{last_fuel_check.strip()}"
                vehicle_data[5] = f"{fuel_consumed.strip()} litres"

                lines[i] = " | ".join(vehicle_data) + "\n"
                break

        if updated:
            with open("./database_admin/fuel_data.txt", 'w') as file:
                file.writelines(lines)
            print(f"Fuel data for Vehicle ID {vehicle_id} updated successfully.")
        else:
            print(f"Vehicle with ID {vehicle_id} not found.")

    except FileNotFoundError:
        print("Fuel data file not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")


def track_fuel_consumption(session):
    print("---------------Track Fuel Consumption Patterns---------------")

    try:
        driver_email = input("Enter Driver's Email: ")
        route_used = input("Enter the route used (Route 1 or Route 2): ")

        with open("./database_driver/delivery_details_for_admin_report.txt", "r") as file:
            found = False
            for line in file:
                delivery_data = line.strip().split(" | ")

                if delivery_data[0] == driver_email:
                    found = True

                    distance_traveled = float(delivery_data[6])
                    fuel_used = float(delivery_data[12])

                    if distance_traveled <= 0 or fuel_used <= 0:
                        print("Distance traveled and fuel used must be positive values.")
                        return

                    fuel_consumption_l_per_100km = (fuel_used / distance_traveled) * 100

                    print("\n---------------Fuel Consumption Report---------------")
                    print(f"Driver's Email: {driver_email}")
                    print(f"Route Used: {route_used}")
                    print(f"Distance Traveled: {distance_traveled:.2f} km")
                    print(f"Fuel Consumed: {fuel_used:.2f} liters")
                    print(f"Fuel Consumption: {fuel_consumption_l_per_100km:.2f} liters/100 km")
                    break

            if not found:
                print(f"Driver with email {driver_email} not found in the delivery data.")

    except FileNotFoundError:
        print("The delivery data file was not found. Please ensure the file exists.")
    except ValueError:
        print("Invalid input. Please enter numeric values for distance and fuel.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def check_low_fuel_alerts(session):
    try:
        while True:
            try:
                fuel_threshold = float(input("Enter the fuel level threshold (in %): "))
                if fuel_threshold < 0 or fuel_threshold > 100:
                    print("Please enter a valid fuel percentage between 0 and 100.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the fuel level threshold.")

        with open("./database_admin/fuel_data.txt", 'r') as file:
            lines = file.readlines()

        alerts = []

        for line in lines:
            vehicle_detail = line.strip().split(' | ')

            try:
                fuel_level_str = vehicle_detail[2].strip()

                if "%" in fuel_level_str:
                    fuel_level = float(fuel_level_str.strip('%'))
                else:
                    fuel_level = float(fuel_level_str)

            except (IndexError, ValueError) as e:
                print(f"Error parsing fuel level for line: {line}. Error: {e}")
                continue

            if fuel_level <= fuel_threshold:
                alerts.append(
                    f"Vehicle ID: {vehicle_detail[0]} (Model: {vehicle_detail[1]}) has low fuel: {fuel_level}%.")

        if alerts:
            print("\nLow Fuel Alerts:\n")
            for alert in alerts:
                print(alert)
        else:
            print(f"No vehicles with fuel levels below or equal to {fuel_threshold}%.")

    except FileNotFoundError:
        print("Fuel data file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")










