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
            else:
                return profile


def create_user(user):
    filename = "./database/user.txt"
    new_user = '\n' + user[0] + ' | '+ user[1] + ' | ' + user[2] + '\n'

    with open(filename, 'a') as file:
        file.write(new_user)


def create_driver(driver_detail):
    filename = "./database/driver_profile.txt"
    new_driver = (
            '\n' +
            driver_detail[0] + ' | '+
            driver_detail[1] +' | '+
            driver_detail[2]+' | '+
            driver_detail[3]+' | '+
            driver_detail[4]+' | '+
            driver_detail[5]+' | '+
            driver_detail[6]+' | '+
            driver_detail[7]+
            '\n')

    with open(filename, 'a') as file:
        file.write(new_driver)

    print("Success")
    return

# def update_user()

# def delete_user()