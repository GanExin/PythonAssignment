from PythonAssignment.auth.validation.driver_validation import validate_driver_availability_status, \
    validate_driver_health_report, \
    get_health_report_value, validate_password, validate_first_name, \
    validate_last_name, validate_number, validate_address
from PythonAssignment.database import read_users, update_password_to_db, read_driver_details, \
    update_driver_first_name_to_db, update_driver_last_name_to_db, update_driver_phone_number_to_db, \
    update_driver_address_to_db, update_driver_availability_status_to_db, update_driver_license_to_db, \
    update_driver_health_report_to_db, update_driver_dependencies_to_db, display_driver_details

#function to update user's password
def update_password(session):
    users = read_users() #set all lines in user.txt as users
    current_user = session[0] #check if current user match email aka session[0]

    for user in users:
        db_email = user[0]
        if current_user == db_email: #ensure current_user match database email
            while True:
                print("\n---------------------Update New Password---------------------\n")
                new_password = input(f"Your current password is {user[1]}. Please input new password: ") #user[1] == database password

                if validate_password(new_password):
                    user[1] = new_password #set new password as database password
                    update_password_to_db(users) #update new password to database
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
                print("\n---------------------Update New Profile---------------------\n")
                choice = input("Please select a number to update? "
                                "\n[1]first name \n[2]last name \n[3]phone number \n[4]address "
                                "\n[5]availability status \n[6]driver license \n[7]health report "
                               "\n[8]Number of family dependencies \n[9]exit: ")

                if choice == '1':
                    while True:
                        update_driver_first_name = input(f"Your current first name is {driver[1]}. Please enter new first name: ").capitalize()
                        if validate_first_name(update_driver_first_name):
                            driver[1] = update_driver_first_name
                            update_driver_first_name_to_db(driver)
                            print(f"\n⭐{driver[1]} successfully updated for email: {user[0]} !⭐ \n")
                            print(display_driver_details(driver))
                            break

                elif choice == '2':
                    while True:
                        update_driver_last_name = input(f"Your current last name is {driver[2]}. Please enter new last name: ").capitalize()
                        if validate_last_name(update_driver_last_name):
                            driver[2] = update_driver_last_name
                            update_driver_last_name_to_db(driver)
                            print(f"\n⭐{driver[2]} successfully updated for email: {user[0]} !⭐ \n")
                            print(display_driver_details(driver))
                            break

                elif choice == '3':
                    while True:
                        update_driver_phone_number = input(f"Your current phone number is {driver[3]}. Please enter new phone number: ")
                        if validate_number(update_driver_phone_number):
                            driver[3] = update_driver_phone_number
                            update_driver_phone_number_to_db(driver)
                            print(f"\n⭐{driver[3]} successfully updated for email: {user[0]} !⭐ \n")
                            print(display_driver_details(driver))
                            break

                elif choice == '4':
                    while True:
                        update_driver_address = input(f"Your current address is {driver[4]}. Please enter new address: ")
                        if validate_address(update_driver_address):
                            driver[4] = update_driver_address
                            update_driver_address_to_db(driver)
                            print(f"\n⭐{driver[4]} successfully updated for email: {user[0]} !⭐ \n")
                            print(display_driver_details(driver))
                            break

                elif choice == '5':
                    while True:
                        update_driver_availability_status = input(f"Your current availability status is {driver[5]}. Please enter new status [available/unavailable]: ").lower()
                        if validate_driver_availability_status(update_driver_availability_status):
                            driver[5] = update_driver_availability_status
                            update_driver_availability_status_to_db(driver)
                            print(f"\n⭐{driver[5]} successfully updated for email: {user[0]} !⭐ \n")
                            print(display_driver_details(driver))
                            break

                elif choice == '6':
                    while True:
                        update_driver_license = input(f"Your current driver license is {driver[6]}. Please enter new driver license: ")
                        if validate_number(update_driver_license):
                            driver[6] = update_driver_license
                            update_driver_license_to_db(driver)
                            print(f"\n⭐{driver[6]} successfully updated for email: {user[0]} !⭐ \n")
                            print(display_driver_details(driver))
                            break

                elif choice == '7':
                    while True:
                        update_driver_health_report = input(f"Your current health report is {driver[7]}. Please enter new health report [1]fit to drive  [2]not fit to drive: ")
                        if validate_driver_health_report(update_driver_health_report):
                            driver[7] = get_health_report_value(update_driver_health_report)
                            update_driver_health_report_to_db(driver)
                            print(f"\n⭐{driver[7]} successfully updated for email: {user[0]} !⭐ \n")
                            print(display_driver_details(driver))
                            break

                elif choice == '8':
                    while True:
                        update_driver_dependencies = input(f"Your current number of dependencies is/are {driver[8]}. Please enter new number: ")
                        if validate_number(update_driver_dependencies):
                            driver[8] = update_driver_dependencies
                            update_driver_dependencies_to_db(driver)
                            print(f"\n⭐{driver[8]} successfully updated to email: {user[0]} !⭐ \n")
                            print(display_driver_details(driver))
                            break

                elif choice == '9':
                    return