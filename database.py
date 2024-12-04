
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
                return profile

    return profile

#create_user
def create_user(user):
    filename = "./database/user.txt"
    new_user = user[0] + ' | '+ user[1] + ' | ' + user[2] + '\n'

    with open(filename, 'a') as file:
        file.write(new_user)

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
            driver_detail[7] + '\n')

    with open(filename, 'a') as file:
        file.write(new_driver)

    print("Success")
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

    print("⭐You have successfully registered⭐")
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

    return



# def delete_user()