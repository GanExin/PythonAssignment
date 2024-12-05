from PythonAssignment.auth.validation.driver_validation import validate_driver_password, validate_driver_first_name, \
    validate_driver_last_name, validate_driver_phone_number, validate_driver_address, \
    validate_driver_availability_status, validate_driver_license, validate_driver_health_report, \
    get_health_report_value, validate_driver_family_dependencies
from PythonAssignment.database import read_users, update_password_to_db, read_driver_details, \
    update_driver_first_name_to_db, update_driver_last_name_to_db, update_driver_phone_number_to_db, \
    update_driver_address_to_db, update_driver_availability_status_to_db, update_driver_license_to_db, \
    update_driver_health_report_to_db, update_driver_dependencies_to_db


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
                choice = input("Please select a number to update? "
                                "[1]first name \n[2]last name \n[3]phone number \n[4]address "
                                "\n[5]availability status \n[6]driver license \n[7]health report "
                               "\n[8]Number of family dependencies \n[9]exit]: ")

                if choice == '1':
                    update_driver_first_name = input(f"Your current first name is {driver[1]}. Please enter new first name: ").capitalize()
                    if validate_driver_first_name(update_driver_first_name):
                        driver[1] = update_driver_first_name
                        update_driver_first_name_to_db(driver)
                        print(f"{driver[1]} successfully updated for email: {user[0]} !")
                        return

                if choice == '2':
                    update_driver_last_name = input(f"Your current last name is {driver[2]}. Please enter new last name: ").capitalize()
                    if validate_driver_last_name(update_driver_last_name):
                        driver[2] = update_driver_last_name
                        update_driver_last_name_to_db(driver)
                        print(f"{driver[2]} successfully updated for email: {user[0]} !")
                        return

                if choice == '3':
                    update_driver_phone_number = input(f"Your current phone number is {driver[3]}. Please enter new phone number: ")
                    if validate_driver_phone_number(update_driver_phone_number):
                        driver[3] = update_driver_phone_number
                        update_driver_phone_number_to_db(driver)
                        print(f"{driver[3]} successfully updated for email: {user[0]} !")
                        return

                if choice == '4':
                    update_driver_address = input(f"Your current address is {driver[4]}. Please enter new address: ")
                    if validate_driver_address(update_driver_address):
                        driver[4] = update_driver_address
                        update_driver_address_to_db(driver)
                        print(f"{driver[4]} successfully updated for email: {user[0]} !")
                        return

                if choice == '5':
                    update_driver_availability_status = input(f"Your current availability status is {driver[5]}. Please enter new status [available/unavailable]: ").lower()
                    if validate_driver_availability_status(update_driver_availability_status):
                        driver[5] = update_driver_availability_status
                        update_driver_availability_status_to_db(driver)
                        print(f"{driver[5]} successfully updated for email: {user[0]} !")
                        return

                if choice == '6':
                    update_driver_license = input(f"Your current driver license is {driver[6]}. Please enter new driver license: ")
                    if validate_driver_license(update_driver_license):
                        driver[6] = update_driver_license
                        update_driver_license_to_db(driver)
                        print(f"{driver[6]} successfully updated for email: {user[0]} !")
                        return

                if choice == '7':
                    update_driver_health_report = input(f"Your current health report is {driver[7]}. Please enter new health report [1]fit to drive  [2]not fit to drive: ")
                    if validate_driver_health_report(update_driver_health_report):
                        driver[7] = get_health_report_value(update_driver_health_report)
                        update_driver_health_report_to_db(driver)
                        print(f"{driver[7]} successfully updated for email: {user[0]} !")
                        return

                if choice == '8':
                    update_driver_dependencies = input(f"Your current number of dependencies is/are {driver[8]}. Please enter new number: ")
                    if validate_driver_family_dependencies(update_driver_dependencies):
                        driver[8] = update_driver_dependencies
                        update_driver_dependencies_to_db(driver)
                        print(f"{driver[8]} successfully updated to email: {user[0]} !")
                        return

                if choice == '9':
                    break

                else:
                    print("Invalid input")
                    continue



#print the actual details
#prompt user to chose what to update
