
def manage_fuel_and_consumption(session):
    print("------------------Manage Fuel and Vehicle Consumption------------------")
    while True:
        choice = input("[1] View Fuel Data \n[2] Track Fuel Consumption "
                       "\n[3] Check Low Fuel Alert \n[4] Exit"
                       "\nPlease choose a feature (1/2/3/4): ")
        if choice == '1':
            view_fuel_data(session)
        elif choice == '2':
            track_fuel_consumption(session)
        elif choice == '3':
            check_low_fuel_alerts(session)
        elif choice == '4':
            print("Exiting Manage Fuel and Vehicle Consumption.")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

def view_fuel_data(session):
    print("---------------View Fuel Data---------------")

    try:
        with open("./database_driver/delivery_details_for_admin_report.txt", 'r') as file:
            lines = file.readlines()

            if not lines:
                print("No fuel data found.")
                return

            print("Fuel Data for All Drivers:")
            for line in lines:
                driver_detail = line.strip().split(' | ')
                fuel_data = (f"Driver email: {driver_detail[0]}\n"
                             f"Route: {driver_detail[1]}\n"
                             f"Current fuel level: {driver_detail[9]}%\n"
                             f"Total cost of refuel: RM {driver_detail[10]}\n"
                             f"Total fuel consumption: {driver_detail[12]} litres/km\n")
                print(fuel_data)
                print("-" * 50)

    except FileNotFoundError:
        print("No fuel data file found. Please ensure the delivery details file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def track_fuel_consumption(session):
    print("---------------Track Fuel Consumption Patterns---------------")

    try:
        driver_email = input("Enter Driver's Email: ")

        with open("./database_driver/delivery_details_for_admin_report.txt", "r") as file:
            found = False
            for line in file:
                delivery_data = line.strip().split(" | ")

                if delivery_data[0] == driver_email:
                    found = True

                    route_used = delivery_data[1].strip()
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
        print("File was not found. Please ensure the file exists.")
    except ValueError:
        print("Invalid input. Please ensure numeric values for distance and fuel are correctly formatted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def check_low_fuel_alerts(session):
    print("---------------Check Low Fuel Alerts---------------")
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

        with open("./database_driver/delivery_details_for_admin_report.txt", 'r') as file:
            lines = file.readlines()

        alerts = []

        for line in lines:
            driver_detail = line.strip().split(' | ')

            try:

                fuel_level_str = driver_detail[9].strip()

                if "%" in fuel_level_str:
                    fuel_level = float(fuel_level_str.strip('%'))
                else:
                    fuel_level = float(fuel_level_str)

            except (IndexError, ValueError) as e:
                print(f"Error parsing fuel level for line: {line}. Error: {e}")
                continue

            if fuel_level <= fuel_threshold:
                alert = f"\nDriver email: {driver_detail[0]}\nVehicle has low fuel: {fuel_level}%"
                alerts.append(alert)

        if alerts:
            print("Low Fuel Alerts:")
            for alert in alerts:
                print(alert)
        else:
            print(f"No drivers with fuel levels below or equal to {fuel_threshold}%.")

    except FileNotFoundError:
        print("Details file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")






