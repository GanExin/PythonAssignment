
def reports(session):
    print("------------------Reports------------------")
    # User selects a feature from the menu
    while True:
        choice = input("[1] View Detailed Report \n[2] View Trip-log Report"
                       "\n[3] Exit"
                       "\nPlease choose a feature (1/2/3): ")

        if choice == "1":
            generate_report(session)
        elif choice == '2':
            generate_trip_log_report(session)
        elif choice == '3':
            print("Exiting Reports.")
            break
        else:
            print("Invalid input. Please enter a valid choice.")


def calculate_inventory_turnover_ratio():
    try:
        # Count cancelled orders
        with open("./database_customer/cancelled_orders.txt", 'r') as cancelled_file:
            cancelled_lines = cancelled_file.readlines()
            if not cancelled_lines:
                return "Error: Cancelled orders file is empty."
            cancelled_orders = len(cancelled_lines) // 12

        # Count total orders
        with open("./database_customer/orders.txt", 'r') as total_file:
            total_lines = total_file.readlines()
            if not total_lines:
                return "Error: Total orders file is empty."
            total_orders = len(total_lines) // 12

        if total_orders == 0:
            return "Error: No total orders found."

        # Calculate inventory turnover ratio
        inventory_turnover_ratio = cancelled_orders / total_orders
        return f"Inventory Turnover Ratio: {inventory_turnover_ratio:.2f} (Cancelled Orders: {cancelled_orders}, Total Orders: {total_orders})"

    except FileNotFoundError as e:
        return f"Error: {e.filename} not found."
    except Exception as e:
        return f"An error occurred: {e}"



def calculate_truck_turnaround_time():
    try:
        total_turnaround_time = 0
        total_trips = 0

        with open("./database_driver/delivery_details_for_admin_report.txt", 'r') as file:
            for line in file:
                driver_detail = line.strip().split(' | ')
                start_time = driver_detail[2].strip()
                end_time = driver_detail[3].strip()

                if start_time != "NIL" and end_time != "NIL":
                    start_date, start_hour = start_time.split(";")
                    end_date, end_hour = end_time.split(";")

                    # Extract day values only for simplicity
                    start_day = int(start_date.split('/')[0])
                    end_day = int(end_date.split('/')[0])

                    # Calculate total hours (day difference * 24 + hour difference)
                    turnaround_time = (end_day - start_day) * 24 + (int(end_hour.split(":")[0]) - int(start_hour.split(":")[0]))
                    total_turnaround_time += turnaround_time
                    total_trips += 1

        if total_trips == 0:
            return "Error: No completed trips found."

        average_turnaround_time = total_turnaround_time / total_trips
        return f"Average Truck Turnaround Time: {average_turnaround_time:.2f} hours"

    except FileNotFoundError:
        return "Error: Delivery details file not found."
    except Exception as e:
        return f"An error occurred: {e}"



def calculate_average_transportation_cost():
    total_fuel_cost = 0
    total_trips = 0

    try:
        with open("./database_driver/delivery_details_for_admin_report.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                driver_detail = line.strip().split(' | ')
                total_fuel_cost += float(driver_detail[10].strip())
                total_trips += 1  # Increment the trip count

        if total_trips == 0:
            return "Error: No trips found."

        average_transportation_cost = total_fuel_cost / total_trips  # Calculate the average transportation cost (fuel cost per trip)
        return f"Average Transportation Cost: RM {average_transportation_cost:.2f}"

    except FileNotFoundError:
        return "Error: Delivery details file not found."
    except Exception as e:
        return f"An error occurred: {e}"


def calculate_operating_ratio():
    total_cost_of_refuel = 0
    total_distance_travelled = 0

    try:
        with open("./database_driver/delivery_details_for_admin_report.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                driver_detail = line.strip().split(' | ')
                total_cost_of_refuel += float(driver_detail[10].strip()) # Add the refuel cost
                total_distance_travelled += float(driver_detail[6].strip()) # Add the distance traveled

        if total_distance_travelled == 0:
            return "Error: No distance travelled data found."

        # Calculate the operating ratio
        operating_ratio = (total_cost_of_refuel / total_distance_travelled) * 100
        return f"Operating Ratio: {operating_ratio:.2f}%"

    except FileNotFoundError:
        return "Error: Delivery details file not found."
    except Exception as e:
        return f"An error occurred: {e}"

def generate_report(session):
    print("---------------Key Metrics Report---------------")
    print(calculate_inventory_turnover_ratio())
    print(calculate_truck_turnaround_time())
    print(calculate_average_transportation_cost())
    print(calculate_operating_ratio())


def generate_trip_log_report(session):
    print("---------------Trip Log Report---------------")

    try:
        with open("./database_driver/delivery_details_for_admin_report.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print("No trip data available.")
                return

            for line in lines:
                driver_detail = line.strip().split(' | ')

                print("\n----- Trip Log Details -----")
                print(f"Driver Email: {driver_detail[0]}")
                print(f"Route: {driver_detail[1]}")
                print(f"Start Journey: {driver_detail[2]}")
                print(f"End Journey: {driver_detail[3]}")
                print(f"Driver current location: {driver_detail[5]}")
                print(f"Total Distance Travelled: {driver_detail[6]} km")
                print(f"Fuel Level: {driver_detail[9]}%")
                print(f"Total Fuel Consumption: {driver_detail[12]} litres/km")
                print(f"Cost of Refuel: RM {driver_detail[10]}")
                print(f"Safety Check Status: {driver_detail[11]}")
                print("------------------------------")

    except FileNotFoundError:
        print("Error: Delivery details file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



