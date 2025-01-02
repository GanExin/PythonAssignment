def read_users():
    users = []
    filename = "./database_driver/user.txt"
    with open(filename, 'r') as file:
        for line in file:
            user = []
            col = line.strip().split(" | ")
            user.append(col[0])
            user.append(col[1])
            user.append(col[2])
            users.append(user)

    return users

#read driver details from driver_profile.txt
def read_driver_details(driver_email):
    profile = []
    filename = "./database_driver/driver_profile.txt"
    with open(filename, 'r') as drivers:
        for driver in drivers:
            col = driver.strip().split(" | ")
            email = col[0]
            if driver_email == email:
                profile.append(col[0])
                profile.append(col[1])
                profile.append(col[2])
                profile.append(col[3])
                profile.append(col[4])
                profile.append(col[5])
                profile.append(col[6])
                profile.append(col[7])
                profile.append(col[8])
                profile.append(col[9])
                return profile

    return profile

#read customer details from customer_profile.txt
def read_customer_details(customer_email):
    profile = []
    filename = "./database_customer/customer_profile.txt"
    with open(filename, 'r') as customers:
        for customer in customers:
            col = customer.strip().split(" | ")
            email = col[0]
            if customer_email == email:
                profile.append(col[0])
                profile.append(col[1])
                profile.append(col[2])
                profile.append(col[3])
                return profile
        return profile


#read delivery details from driver_update_for_admin.txt
def read_delivery_details(driver_email):
    details = []
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r') as deliveries:
        for delivery in deliveries:
            col = delivery.strip().split(" | ")
            email = col[0]
            if driver_email == email:
                details.append(col[0])
                details.append(col[1])
                details.append(col[2])
                details.append(col[3])
                details.append(col[4])
                details.append(col[5])
                details.append(col[6])
                details.append(col[7])
                details.append(col[8])
                details.append(col[9])
                details.append(col[10])
                details.append(col[11])
                details.append(col[12])
                return details
        return details

#create delivery_details
def create_delivery_details(delivery_detail):
    filename="./database_driver/delivery_details_for_admin_report.txt"
    new_details = (
            delivery_detail[0]+ ' | ' +
            delivery_detail[1]+ ' | ' +
            delivery_detail[2]+ ' | ' +
            delivery_detail[3]+ ' | ' +
            delivery_detail[4]+ ' | ' +
            delivery_detail[5]+ ' | ' +
            delivery_detail[6]+ ' | ' +
            delivery_detail[7]+ ' | ' +
            delivery_detail[8]+ ' | ' +
            delivery_detail[9] + ' | ' +
            delivery_detail[10] + ' | ' +
            delivery_detail[11] + ' | ' +
            delivery_detail[12] +  '\n')

    with open(filename, 'a') as file:
        file.write(new_details)
    print("\n⭐Details created successfully⭐\n")
    print(display_delivery_details(delivery_detail))
    return

#create user to user.txt
def create_user(user):
    filename = "./database_driver/user.txt"
    new_user = user[0] + ' | '+ user[1] + ' | ' + user[2] + '\n'

    with open(filename, 'a') as file:
        file.write(new_user)

#create admin details to admin_profile.txt
def create_admin(admin_detail):
    filename = "./database_admin/admin_profile.txt"
    new_admin = (
            admin_detail[0] + ' | '+
            admin_detail[1] +' | '+
            admin_detail[2]+' | '+
            admin_detail[3]+' | '+
            admin_detail[4]+' | '+
            admin_detail[5]+ '\n')

    with open(filename, 'a') as file:
        file.write(new_admin)

    print("⭐You have successfully registered⭐ \n")
    print(display_admin_detail(admin_detail))
    return

#create driver details to driver_profile.txt
def create_driver(driver_detail):
    filename = "./database_driver/driver_profile.txt"
    new_driver = (
            driver_detail[0] + ' | '+
            driver_detail[1] +' | '+
            driver_detail[2]+' | '+
            driver_detail[3]+' | '+
            driver_detail[4]+' | '+
            driver_detail[5]+' | '+
            driver_detail[6]+' | '+
            driver_detail[7] +' | '+
            driver_detail[8] + ' | ' +
            driver_detail[9] + '\n')

    with open(filename, 'a') as file:
        file.write(new_driver)

    print("⭐You have successfully registered⭐ \n")
    print(display_driver_details(driver_detail))
    return

#create customer profile to customer_profile.txt
def create_customer(customer_detail):
    filename = "./database_customer/customer_profile.txt"
    new_customer = (
            customer_detail[0] + ' | '+
            customer_detail[1] +' | '+
            customer_detail[2] +' | '+
            customer_detail[3] + '\n')

    with open(filename, 'a') as file:
        file.write(new_customer)

    print("⭐You have successfully registered⭐ \n")
    print(display_customer_detail(customer_detail))
    return

# makes sure orderID continues from last orderID number
def next_order_id():
    try:
        with open("./database_customer/orders.txt", "r") as file:
            max_id = 0
            for line in file:
                # Check if the line starts with "Order ID:"
                line = line.strip()
                if line.startswith("Order ID:"):
                    try:
                        order_id = int(line.split(":")[1].strip())
                        max_id = max(max_id, order_id)
                    except ValueError:
                        pass  # Ignore lines that are invalid
            return max_id + 1  # Return the next Order ID
    except FileNotFoundError:
        return 1  # Start with OrderID 1 if the file doesn't exist

#create order details into orders.txt
def create_order(order_details):
    filename = "./database_customer/orders.txt"
    new_order = (
        f"Order ID: {order_details[0]}\n"
        f"Product Name: {order_details[1]}\n"
        f"Quantity: {order_details[2]}\n"
        f"Customer Name: {order_details[3]}\n"
        f"Address: {order_details[4]}\n"
        f"Phone Number: {order_details[5]}\n"
        f"Payment Method: {order_details[6]}\n"
        f"Vehicle: {order_details[7]}\n"
        f"Special Request: {order_details[8]}\n"
        f"Route: {order_details[9]}\n"
        f"Route Price: RM{order_details[10]}\n"
        f"Delivery status: {order_details[11]}\n"
        f"Status update date: {order_details[12]}\n"
        f"Driver: {order_details[13]}\n"
        + "-" * 40 + "\n"
    )

    with open(filename, 'a') as file:
        file.write(new_order)
    return

#Create review to user_rate_review.txt.txt
def store_rate_review(review):
    filename = "./database_customer/user_rate_review.txt"
    new_review = (
        f"Name: {review[0]}\n"
        f"Rating: {review[1]}\n"
        f"Review: {review[2]}\n"
        + "_" * 40 + "\n"
    )

    with open(filename, 'a') as file:
        file.write(new_review)
    return

#update new password to user.txt
def update_password_to_db(users):
    filename = "./database_driver/user.txt"
    with open(filename, 'w') as file:
        for user in users:
            new_user = user[0]+" | " + user[1] + " | " + user[2] + '\n'
            file.write(new_user)
    return

# def new first name to driver_profile.txt
def update_driver_first_name_to_db(driver):
    filename = "./database_driver/driver_profile.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            driver_detail = line.strip().split(' | ')
            if driver_detail[0] == driver[0]:
                driver_detail[1] = driver[1]
                lines[i] = ' | '.join(driver_detail) + '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()

    return

#update new last name to driver_profile.txt
def update_driver_last_name_to_db(driver):
    filename = "./database_driver/driver_profile.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            driver_detail = line.strip().split(' | ')
            if driver_detail[0] == driver[0]:
                driver_detail[2] = driver[2]
                lines[i] = ' | '.join(driver_detail) + '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()

    return

#update new phone number to driver_profile.txt
def update_driver_phone_number_to_db(driver):
    filename = "./database_driver/driver_profile.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            driver_detail = line.strip().split(' | ')
            if driver_detail[0] == driver[0]:
                driver_detail[3] = driver[3]
                lines[i] = ' | '.join(driver_detail) + '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()

#update new address to driver_profile.txt
def update_driver_address_to_db(driver):
    filename = "./database_driver/driver_profile.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            driver_detail = line.strip().split(' | ')
            if driver_detail[0] == driver[0]:
                driver_detail[4] = driver[4]
                lines[i] = ' | '.join(driver_detail) + '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()

#update new status to driver_profile.txt
def update_driver_availability_status_to_db(driver):
    filename = "./database_driver/driver_profile.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            driver_detail = line.strip().split(' | ')
            if driver_detail[0] == driver[0]:
                driver_detail[5] = driver[5]
                lines[i] = ' | '.join(driver_detail) + '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()

#update new liscense to driver_profile.txt
def update_driver_license_to_db(driver):
    filename = "./database_driver/driver_profile.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            driver_detail = line.strip().split(' | ')
            if driver_detail[0] == driver[0]:
                driver_detail[6] = driver[6]
                lines[i] = ' | '.join(driver_detail) + '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()

#update new report to driver_profile.txt
def update_driver_health_report_to_db(driver):
    filename = "./database_driver/driver_profile.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            driver_detail = line.strip().split(' | ')
            if driver_detail[0] == driver[0]:
                driver_detail[7] = driver[7]
                lines[i] = ' | '.join(driver_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()

#update new family to driver_profile.txt
def update_driver_dependencies_to_db(driver):
    filename = "./database_driver/driver_profile.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            driver_detail = line.strip().split(' | ')
            if driver_detail[0] == driver[0]:
                driver_detail[8] = driver[8]
                lines[i] = ' | '.join(driver_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#update delivery status and date to orders.txt
def update_parcel_details(order_id, new_status, new_date, new_driver):
    filename = "./database_customer/orders.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()
        updated = False

        for orders in range(len(lines)):
            if f"Order ID: {order_id}" in lines[orders]:
                for details in range(orders, len(lines)):
                    if "Delivery status: " in lines[details]:
                        lines[details] = f"Delivery status: {new_status}\n"
                    elif "Status update date: " in lines[details]:
                        lines[details] = f"Status update date: {new_date}\n"
                    elif "Driver: " in lines[details]:
                        lines[details] = f"Driver: {new_driver}\n"
                    elif "----------------------------------------" in lines[details]:
                        updated = True
                        break
            if updated:
                break

        if updated:
            file.seek(0)
            file.writelines(lines)
            file.truncate()
            print(f"Order ID {order_id} has been updated!\n")
        else:
            print(f"Order ID {order_id} not found.")
    return

#update route to delivery_details_for_admin_report.txt
def update_route_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[1] = detail[1]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#update s_journey_datetime to delivery_details_for_admin_report.txt
def update_s_journey_date_time_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[2] = detail[2]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#update e_journey_datetime to delivery_details_for_admin_report.txt
def update_e_journey_date_time_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[3] = detail[3]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#update turnaround_time to delivery_details_for_admin_report.txt
def update_turnaround_time_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[4] = detail[4]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

def update_current_location_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[5] = detail[5]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break
        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#update total_distances_travelled to delivery_details_for_admin_report.txt
def update_total_distance_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[6] = detail[6]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#update total_refuels to delivery_details_for_admin_report.txt
def update_total_refuel_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[7] = detail[7]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#update total_stopover to delivery_details_for_admin_report.txt
def update_total_stopover_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[8] = detail[8]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#update current_fuel_level to delivery_details_for_admin_report.txt
def update_current_fuel_level_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[9] = detail[9]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#update total_cost_of_refuel to delivery_details_for_admin_report.txt
def update_total_cost_of_refuel_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[10] = detail[10]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#update safety_cleaning_status to delivery_details_for_admin_report.txt
def update_safety_cleaning_status_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[11] = detail[11]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#update total_fuel_consumption to delivery_details_for_admin_report.txt
def update_total_fuel_consumption_to_db(detail):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r+') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            delivery_detail = line.strip().split(' | ')
            if delivery_detail[0] == detail[0]:
                delivery_detail[12] = detail[12]
                lines[i] = ' | '.join(delivery_detail)+ '\n'
                break

        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return

#display all driver details from driver_profile.txt
def display_driver_details(driver):
    filename = "./database_driver/driver_profile.txt"
    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            driver_detail = line.strip().split(' | ')
            if driver_detail[0] == driver[0]:
                vehicle = driver_detail[9] if driver_detail[9] != "None" else "No vehicle assigned"
                detail = (f"Role: Driver \n"
                          f"Email: {driver[0]} \n"
                          f"First Name: {driver[1]} \n"
                          f"Last Name: {driver[2]} \n"
                          f"Phone Number: {driver[3]} \n"
                          f"Address: {driver[4]} \n"
                          f"Availability Status: {driver[5]} \n"
                          f"Driver License: {driver[6]} \n"
                          f"Health Report: {driver[7]} \n"
                          f"Number of Family Dependencies: {driver[8]} \n"
                          f"Assigned Vehicle ID: {vehicle}")
                return detail

#display all admin details from admin_profile.txt
def display_admin_detail(admin):
    filename = "./database_admin/admin_profile.txt"
    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            admin_detail = line.strip().split(' | ')
            if admin_detail[0] == admin[0]:
                detail = (f"Role: Admin \n"
                          f"Email: {admin[0]} \n"
                          f"First Name: {admin[1]} \n"
                          f"Last Name: {admin[2]} \n"
                          f"Date of birth: {admin[3]} \n"
                          f"Phone Number: {admin[4]} \n"
                          f"Address: {admin[5]}")
                return detail

#display all customer details from customer_profile.txt
def display_customer_detail(customer):
    filename = "./database_customer/customer_profile.txt"
    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            customer_detail = line.strip().split(' | ')
            if customer_detail[0] == customer[0]:
                detail = (f"Role: Customer \n"
                          f"Email: {customer[0]} \n"
                          f"Full Name: {customer[1]} \n"
                          f"Phone Number: {customer[2]} \n"
                          f"Address: {customer[3]}")
                return detail

#display all delivery details from delivery_details_for_admin_report.txt
def display_delivery_details(delivery):
    filename = "./database_driver/delivery_details_for_admin_report.txt"
    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            driver_detail = line.strip().split(' | ')
            if driver_detail[0] == delivery[0]:
                detail = (f"Driver email: {delivery[0]} \n"
                          f"Route: {delivery[1]} \n"
                          f"Start journey date; time: {delivery[2]} \n"
                          f"End journey data; time: {delivery[3]} \n"
                          f"Turnaround time: {delivery[4]} hours\n"
                          f"Driver current location: {delivery[5]}\n"
                          f"Total distance travelled: {delivery[6]} km \n"
                          f"Total refuels: {delivery[7]} \n"
                          f"Total stopovers: {delivery[8]} \n"
                          f"Current fuel level: {delivery[9]} % \n"
                          f"Total cost of refuel: RM {delivery[10]} \n"
                          f"Safety, cleaning and fuel check status: {delivery[11]}\n"
                          f"Total fuel consumption: {delivery[12]} litres/km")
                return detail

#display order details from orders.txt
def display_order(order_id):
    filename = "./database_customer/orders.txt"
    with open(filename, 'r') as file:
        lines = file.readlines()
        orders = [] #list to store all orders
        current_order = {}

        for line in lines:
            line = line.strip()
            if line == "----------------------------------------":
                if current_order:
                    orders.append(current_order)
                current_order = {}
            elif ": " in line:
                key, value = line.split(": ", 1)
                current_order[key] = value
        if current_order:
            orders.append(current_order)

        for order in orders:
            if order.get("Order ID") == str(order_id):
                    detail = (f"Order ID: {order.get('Order ID')}\n"
                              f"Product Name: {order.get('Product Name')}\n"
                              f"Quantity: {order.get('Quantity')}\n"
                              f"Customer Name: {order.get('Customer Name')}\n"
                              f"Address: {order.get('Address')}\n"
                              f"Phone Number: {order.get('Phone Number')}\n"
                              f"Payment Method: {order.get('Payment Method')}\n"
                              f"Vehicle: {order.get('Vehicle')}\n"
                              f"Special Request: {order.get('Special Request')}\n"
                              f"Route: {order.get('Route')}\n"
                              f"Route Price: RM{order.get('Route Price')}\n"
                              f"Delivery status: {order.get('Delivery status')}\n"
                              f"Status update date: {order.get('Status update date')}\n"
                              f"Driver: {order.get('Driver')}")
                    return detail

        print(f"Order ID {order_id} not found. "
              f"\nPossible reasons: \nCustomer cancelled order/Order ID does not exist.")
        return

def display_available_order():
    filename = "./database_customer/orders.txt"
    with open(filename, 'r') as file:
        lines = file.readlines()
        orders = [] #list to store all orders
        current_order = {}

        for line in lines:
            line = line.strip()
            if line == "----------------------------------------":
                if current_order:
                    orders.append(current_order)
                current_order = {}
            elif ": " in line:
                key, value = line.split(": ", 1)
                current_order[key] = value
        if current_order:
            orders.append(current_order)

        #Set requirements
        match_delivery_status = "Undelivered"
        match_status_update_date= "NIL"
        match_driver = "NIL"

        #Check requirements
        available_jobs = [
            order for order in orders
            if order.get("Delivery status") == match_delivery_status and
               order.get("Status update date") == match_status_update_date and
               order.get("Driver") == match_driver
        ]

        if not available_jobs:
            return "No available orders found.", []

        print_jobs_available = ""
        order_ids = []
        for order in available_jobs:
            order_id = order.get('Order ID')
            order_ids.append(order_id)
            detail = (f"Order ID: {order_id}\n"
                      f"Product Name: {order.get('Product Name')}\n"
                      f"Quantity: {order.get('Quantity')}\n"
                      f"Customer Name: {order.get('Customer Name')}\n"
                      f"Address: {order.get('Address')}\n"
                      f"Phone Number: {order.get('Phone Number')}\n"
                      f"Payment Method: {order.get('Payment Method')}\n"
                      f"Vehicle: {order.get('Vehicle')}\n"
                      f"Special Request: {order.get('Special Request')}\n"
                      f"Route: {order.get('Route')}\n"
                      f"Route Price: {order.get('Route Price')}\n"
                      f"Delivery status: {order.get('Delivery status')}\n"
                      f"Status update date: {order.get('Status update date')}\n"
                      f"Driver: {order.get('Driver')}\n"
                      + "-" * 40 + "\n")
            print_jobs_available += detail

        return print_jobs_available, order_ids

#display matching orders by driver email
def display_driver_jobs(driver_email):
    filename = "./database_customer/orders.txt"
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            driver_orders = []
            current_order = {}

            for line in lines:
                line = line.strip()
                if line == "----------------------------------------":
                    if current_order and current_order.get("Driver") == driver_email:  #Match the driver email
                        detail = format_order_details(current_order)
                        driver_orders.append(detail)
                    current_order = {}
                elif ": " in line:
                    key, value = line.split(": ", 1)
                    current_order[key] = value
            if driver_orders:
                return "\n\n".join(driver_orders)
            else:
                return f"No jobs found for driver: {driver_email}, please book parcels first."
    except FileNotFoundError:
        print("Order file not found.")
        return None

#return dictionary as key-value pair separated by newlines
def format_order_details(order):
    return "\n".join([f"{key}: {value}" for key, value in order.items()])

#Check if driver booked a parcel from orders.txt
def check_driver_parcel(current_user):
    filename = "./database_customer/orders.txt"
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: Unable to find orders in Orders database.")
        return False
    for i in range(len(lines)):
        if lines[i].startswith("Driver:"): #check only if line starts with "Driver: "
            driver_email = lines[i].split("Driver:")[1].strip()
            if driver_email == current_user: #check if driver is same as current user
                return True
    return False

def display_vehicle_data(vehicle_data):
    filename = "./database_admin/vehicle_data.txt"
    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            vehicle_detail = line.strip().split(' | ')

            if vehicle_detail[0] == vehicle_data[0]:
                if len(vehicle_detail) > 5:
                    maintenance_history = vehicle_detail[5].split('|')
                    maintenance_details = "\n".join([f"  - {item}" for item in maintenance_history])
                else:
                    maintenance_details = "No maintenance history available."

                if len(vehicle_detail) > 6:
                    cargo_suitability = vehicle_detail[6]
                else:
                    cargo_suitability = "Not specified."

                detail = (f"Vehicle ID: {vehicle_detail[0]} \n"
                          f"Model: {vehicle_detail[1]} \n"
                          f"Last Inspection: {vehicle_detail[2]} \n"
                          f"Next Inspection: {vehicle_detail[3]} \n"
                          f"Performance: {vehicle_detail[4]} \n"
                          f"Maintenance History: \n{maintenance_details} \n"
                          f"Suitable for Cargo: {cargo_suitability} \n")
                return detail
    return "Vehicle not found in the database."


def store_driver_comment(driver_email, comment):
    filename = "./database_admin/driver_comment.txt"
    new_comment = f"Email: {driver_email}\nComment: {comment}\n\n"

    with open(filename, "a") as file:
        file.write(new_comment)

    print(f"Comment stored successfully")


def display_fuel_data(vehicle):
    filename = "./database_admin/fuel_data.txt"
    with open(filename, 'r') as file:
            lines = file.readlines()

            for line in lines:
                vehicle_detail = line.strip().split(' | ')
                if vehicle_detail[0] == vehicle[0]:
                    detail = (f"Vehicle ID: {vehicle_detail[0]} \n"
                              f"Vehicle Model: {vehicle_detail[1]} \n"
                              f"Fuel Level: {vehicle_detail[2]} \n"
                              f"Mileage: {vehicle_detail[3]} \n"
                              f"Last Fuel Check: {vehicle_detail[4]} \n"
                              f"Fuel Consumed: {vehicle_detail[5]} ")

                    return detail

