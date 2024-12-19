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

                current_fuel_level = vehicle_data[2].split(": ")[1].strip()
                current_mileage = vehicle_data[3].split(": ")[1].strip()
                current_last_check = vehicle_data[4].split(": ")[1].strip()
                current_fuel_consumed = vehicle_data[5].splt(": ")[1].strip()

                fuel_level = input(f"Enter new Fuel Level (current: {current_fuel_level}): ")
                mileage = input(f"Enter new Mileage (current: {current_mileage}): ")
                last_fuel_check = input(f"Enter new fuel check (current: {current_last_check}): ")
                fuel_consumed = input(f"Enter new Fuel Consumed: (current: {current_fuel_consumed})")

                vehicle_data[2] = fuel_level
                vehicle_data[3] = mileage
                vehicle_data[4] = last_fuel_check
                vehicle_data[5] = fuel_consumed

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
        vehicle_id = input("Enter Vehicle ID: ")
        route_used = input("Enter the route used (Route 1 or Route 2): ")
        distance_traveled = float(input("Enter Distance Traveled (in km): "))
        fuel_used = float(input("Enter Fuel Consumed (in liters): "))

        if distance_traveled <= 0 or fuel_used <= 0:
            print("Distance traveled and fuel used must be positive values.")
            return

        fuel_efficiency_km_per_l = distance_traveled / fuel_used
        fuel_efficiency_l_per_100km = (fuel_used / distance_traveled) * 100

        print("\n---------------Fuel Consumption Report---------------")
        print(f"Vehicle ID: {vehicle_id}")
        print(f"Route Used: {route_used}")
        print(f"Distance Traveled: {distance_traveled:.2f} km") # ensures the number is formatted to 2 decimal places
        print(f"Fuel Consumed: {fuel_used:.2f} liters")
        print(f"Fuel Efficiency: {fuel_efficiency_km_per_l:.2f} km/l")
        print(f"Fuel Consumption: {fuel_efficiency_l_per_100km:.2f} liters/100 km")

    except ValueError:
        print("Invalid input. Please enter numeric values for distance and fuel.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def check_low_fuel_alerts(session):
    try:
        fuel_threshold = float(input("Enter the fuel level threshold (in %): "))

        with open("./database_admin/fuel_data.txt", 'r') as file:
            lines = file.readlines()

        alerts = []
        for line in lines:
            vehicle_detail = line.strip().split(' | ')

            try:
                fuel_level_str = vehicle_detail[2].split(":")[1].strip() # Extract and clean the fuel level string
                fuel_level = float(fuel_level_str.strip('%')) # Remove the '%' and convert the fuel level to a float
            except (IndexError, ValueError) as e:
                print(f"Error parsing fuel level for line: {line}. Error: {e}")
                continue

            if fuel_level <= fuel_threshold:
                alerts.append(
                    f"Vehicle ID: {vehicle_detail[0]} (Model: {vehicle_detail[1]}) has low fuel: {fuel_level}%.")

        if alerts:
            return "\n".join(alerts)
        else:
            return "No vehicles with fuel levels below the specified threshold."

    except FileNotFoundError:
        return "Fuel data file not found."
    except ValueError:
        return "Invalid input. Please enter a valid number for the fuel level threshold."
    except Exception as e:
        return f"An error occurred: {e}"









