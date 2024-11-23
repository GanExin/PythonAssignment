from PythonAssignment.auth.validation.driver_validation import validate_driver_email, validate_driver_password, \
    validate_driver_first_name, validate_driver_last_name, validate_driver_phone_number, validate_driver_address, \
    validate_driver_availability_status, validate_driver_license, validate_driver_health_report, get_health_report_value
from PythonAssignment.database import create_user, create_driver


def register():
    while True:
        choice = input("Which role would you like to register as? [customer/admin/driver] or [exit]: ").lower()
        if choice == "customer":
            register_customer()
        elif choice == "driver":
            register_driver()
        elif choice == "admin":
            register_admin()
        elif choice == "exit":
            return
        else:
            print("invalid role")
            continue

def register_customer():
    print("customer registration")

def register_driver():
    role = 'driver'
    email = None
    password = None
    first_name = None
    last_name = None
    phone_number = None
    address = None
    availability_status = None
    driver_license = None
    health_report = None
    while True:
        if email is None:
            email_input = str(input("Please enter email: "))
            if validate_driver_email(email_input):
                email = email_input
            else:
                continue
        if password is None:
            password_input = str(input("Please enter password: "))
            if validate_driver_password(password_input):
                password = password_input
            else:
                continue
        if first_name is None:
            first_name_input = str(input("Please enter first name: "))
            if validate_driver_first_name(first_name_input):
                first_name = first_name_input
            else:
                continue
        if last_name is None:
            last_name_input = str(input("Please enter last name: "))
            if validate_driver_last_name(last_name_input):
                last_name = last_name_input
            else:
                continue
        if phone_number is None:
            phone_number_input = input("Please enter phone number: ")
            if validate_driver_phone_number(phone_number_input):
                phone_number = phone_number_input
            else:
                continue
        if address is None:
            address_input = input("Please enter address: ")
            if validate_driver_address(address_input):
                address = address_input
            else:
                continue
        if availability_status is None:
            availability_status_input = str(input("Are you available to drive? Please enter either 'available' or 'unavailable': ")).lower()
            if validate_driver_availability_status(availability_status_input):
                availability_status = availability_status_input
            else:
                continue
        if driver_license is None:
            driver_license_input = input("Please enter driver license: ")
            if validate_driver_license(driver_license_input):
                driver_license = driver_license_input
            else:
                continue
        if health_report is None:
            health_report_input = input("Are you fit to drive? Please select the following option: [1]Fit to drive, [2]Not fit to drive: ")
            if validate_driver_health_report(health_report_input):
                health_report = get_health_report_value(health_report_input)
            else:
                continue
        break


    user = [email, password, role]
    create_user(user)

    driver_detail = [email, first_name, last_name, phone_number, address, availability_status, driver_license, health_report]
    create_driver(driver_detail)


def register_admin():
    print("admin registration")

