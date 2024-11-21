from PythonAssignment.auth.validation.driver_validation import validate_driver_password, validate_driver_first_name, \
    validate_driver_last_name
from PythonAssignment.database import read_users, update_password_to_db, read_driver_details, update_first_name_to_db, \
    update_last_name_to_db


def update_password(session):
    users = read_users()
    current_user = session[0]

    for user in users:
        db_email = user[0]
        if current_user == db_email:
            while True:
                new_password = input("Please input new password: ")

                if validate_driver_password(new_password):
                    user[1] = new_password
                    update_password_to_db(users)
                    print(f"Password updated for email: {user[0]} !")
                    return

    print("User email does not match.")

def update_profile(session):
    users = read_users()
    current_user = session[0]

    driver = read_driver_details(current_user)

    for user in users:
        db_email = user[0]
        if current_user == db_email:
            while True:
                choice = input("What would you like to update? "
                                              "[first name/last name/phone number/address"
                                              "/availability status/driver license/health report/exit]: ").lower()

                if choice == 'first name':
                    update_first_name = input(f"Your current first name is {driver[1]}. Please enter new first name: ").capitalize()
                    if validate_driver_first_name(update_first_name):
                        driver[1] = update_first_name
                        update_first_name_to_db(driver)
                        print(f"{driver[1]} successfully updated for email: {user[0]} !")
                        return

                if choice == 'last name':
                    update_last_name = input(f"Your current last name is {driver[2]}. Please enter new last name: ").capitalize()
                    if validate_driver_last_name(update_last_name):
                        driver[2] = update_last_name
                        update_last_name_to_db(driver)
                        print(f"{driver[2]} successfully updated for email: {user[0]} !")
                        return

                if choice == 'exit':
                    break


    # print("driver's details")


#print the actual details
#prompt user to chose what to update
