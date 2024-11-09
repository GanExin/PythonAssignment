def read_users():
    users = {}
    filename = "./database/user.txt"
    with open(filename, 'r') as file:
        for line in file:
            col = line.strip().split(" | ")
            email = col[0]
            password = col[1]
            role = col[2]

            users[email] = {
                "email" : email,
                "password": password,
                "role": role,
            }

    return users

def read_driver_details(driver_email):
    driver = {}
    filename = "./database/driver_profile.txt"
    with open(filename, 'r') as file:
        for line in file:
            col = line.strip().split(" | ")
            email = col[0]
            if driver_email == email:
                driver['first_name'] = col[1]
                driver['last_name'] = col[2]
                driver['phone_number'] = col[3]
                driver['address'] = col[4]
                driver['availability_status'] = col[5]
                driver['driver_license'] = col[6]
                driver['health_report'] = col[7]
                return driver
            else:
                return driver


# def create_user()

# def update_user()

# def delete_user()