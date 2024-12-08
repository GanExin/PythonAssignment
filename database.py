def read_users():
    users = []
    filename = "./database/user.txt"
    with open(filename, 'r') as file:
        for line in file:
            user = []
            col = line.strip().split(" | ")
            user.append(col[0])
            user.append(col[1])
            user.append(col[2])
            users.append(user)

    return users

#function to read driver_profile.txt
def read_driver_details(driver_email):
    profile = []
    filename = "./database/driver_profile.txt"
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
                return profile

    return profile

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


#create user.txt
def create_user(user):
    filename = "./database/user.txt"
    new_user = user[0] + ' | '+ user[1] + ' | ' + user[2] + '\n'

    with open(filename, 'a') as file:
        file.write(new_user)


#create_admin
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

#create_driver
def create_driver(driver_detail):
    filename = "./database/driver_profile.txt"
    new_driver = (
            driver_detail[0] + ' | '+
            driver_detail[1] +' | '+
            driver_detail[2]+' | '+
            driver_detail[3]+' | '+
            driver_detail[4]+' | '+
            driver_detail[5]+' | '+
            driver_detail[6]+' | '+
            driver_detail[7] +' | '+
            driver_detail[8] + '\n')

    with open(filename, 'a') as file:
        file.write(new_driver)

    print("⭐You have successfully registered⭐ \n")
    print(display_driver_details(driver_detail))
    return

#create_customer
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

#function to save order details into order.txt
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
        + "-" * 40 + "\n"
    )

    with open(filename, 'a') as file:
        file.write(new_order)
    return

#Save and store review to user_rate_review.txt
def store_rate_review(review):
    filename = "./database_customer/user_rate_review"
    new_review = (
        f"Name: {review[0]}\n"
        f"Rating: {review[1]}\n"
        f"Review: {review[2]}\n"
        + "_" * 40 + "\n"
    )

    with open(filename, 'a') as file:
        file.write(new_review)
    return

# def update_user()
def update_password_to_db(users):
    filename = "./database/user.txt"
    with open(filename, 'w') as file:
        for user in users:
            new_user = user[0]+" | " + user[1] + " | " + user[2] + '\n'
            file.write(new_user)
    return

# def update_driver_profile()
def update_driver_first_name_to_db(driver):
    filename = "./database/driver_profile.txt"
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

def update_driver_last_name_to_db(driver):
    filename = "./database/driver_profile.txt"
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

def update_driver_phone_number_to_db(driver):
    filename = "./database/driver_profile.txt"
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

def update_driver_address_to_db(driver):
    filename = "./database/driver_profile.txt"
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

def update_driver_availability_status_to_db(driver):
    filename = "./database/driver_profile.txt"
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

def update_driver_license_to_db(driver):
    filename = "./database/driver_profile.txt"
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

def update_driver_health_report_to_db(driver):
    filename = "./database/driver_profile.txt"
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

def update_driver_dependencies_to_db(driver):
    filename = "./database/driver_profile.txt"
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

def display_driver_details(driver):
    filename = "./database/driver_profile.txt"
    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            driver_detail = line.strip().split(' | ')
            if driver_detail[0] == driver[0]:
                detail = (f"Role: Driver \n"
                          f"Email: {driver[0]} \n"
                          f"First Name: {driver[1]} \n"
                          f"Last Name: {driver[2]} \n"
                          f"Phone Number: {driver[3]} \n"
                          f"Address: {driver[4]} \n"
                          f"Availability Status: {driver[5]} \n"
                          f"Driver License: {driver[6]} \n"
                          f"Health Report: {driver[7]} \n"
                          f"Number of Family Dependencies: {driver[8]}")
                return detail

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


# def delete_user()