from PythonAssignment.auth.validation.admin_validation import validate_date_of_birth
from PythonAssignment.auth.validation.customer_validation import validate_customer_fullname
from PythonAssignment.auth.validation.driver_validation import validate_driver_availability_status, validate_driver_license, validate_driver_health_report, \
    get_health_report_value, validate_driver_family_dependencies, validate_email, validate_password, \
    validate_first_name, validate_last_name, validate_phone_number, validate_address
from PythonAssignment.database import create_user, create_driver, create_customer, create_admin


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
    print("---------------------Customer Registration---------------------")
    print("Welcome, please enter the details below and register as a customer to Ship2GO.\n")

    role = 'customer'
    email = None
    password = None
    fullname = None
    phone_number = None
    address = None

    while True:
        if email is None:
            email_input = str(input("Please enter email: "))
            if validate_email(email_input):
                email = email_input
            else:
                continue
        if password is None:
            password_input = str(input("Please enter password: "))
            if validate_password(password_input):
                password = password_input
            else:
                continue
        if fullname is None:
            fullname_input = str(input("Please enter Full Name: "))
            if validate_customer_fullname(fullname_input):
                fullname = fullname_input
            else:
                continue
        if phone_number is None:
            phone_number_input = input("Please enter phone number: ")
            if validate_phone_number(phone_number_input):
                phone_number = phone_number_input
            else:
                continue
        if address is None:
            address_input = input("Please enter your address: ")
            if validate_address(address_input):
                address = address_input
            else:
                continue
        break

    user = [email, password, role]
    create_user(user)

    customer_detail = [email, fullname, phone_number, address]
    create_customer(customer_detail)


def register_driver():
    print("---------------------Driver Registration---------------------")
    print("Welcome, please enter the details below and register as a driver to Ship2GO.\n")

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
    family_dependencies = None
    while True:
        if email is None:
            email_input = str(input("Please enter email: "))
            if validate_email(email_input):
                email = email_input
            else:
                continue
        if password is None:
            password_input = str(input("Please enter password: "))
            if validate_password(password_input):
                password = password_input
            else:
                continue
        if first_name is None:
            first_name_input = str(input("Please enter first name: "))
            if validate_first_name(first_name_input):
                first_name = first_name_input
            else:
                continue
        if last_name is None:
            last_name_input = str(input("Please enter last name: "))
            if validate_last_name(last_name_input):
                last_name = last_name_input
            else:
                continue
        if phone_number is None:
            phone_number_input = input("Please enter phone number: ")
            if validate_phone_number(phone_number_input):
                phone_number = phone_number_input
            else:
                continue
        if address is None:
            address_input = input("Please enter address: ")
            if validate_address(address_input):
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
        if family_dependencies is None:
            family_dependencies_input = input("Please enter a number for you number of dependencies: ")
            if validate_driver_family_dependencies(family_dependencies_input):
                family_dependencies = family_dependencies_input
            else:
                continue

        break


    user = [email, password, role]
    create_user(user)

    driver_detail = [email, first_name, last_name, phone_number, address, availability_status, driver_license, health_report, family_dependencies]
    create_driver(driver_detail)


def register_admin():
    print("---------------------Admin Registration---------------------")
    print("Welcome, please enter the details below and register as a admin to Ship2GO.\n")

    role = 'admin'
    email = None
    password = None
    first_name = None
    last_name = None
    date_of_birth = None
    phone_number = None
    address = None
    while True:
        if email is None:
            email_input = str(input("Please enter email: "))
            if validate_email(email_input):
                email = email_input
            else:
                continue
        if password is None:
            password_input = str(input("Please enter your password: "))
            if validate_password(password_input):
                password = password_input
            else:
                continue
        if first_name is None:
            first_name_input = str(input("Please enter your first name: "))
            if validate_first_name(first_name_input):
                first_name = first_name_input
            else:
                continue
        if last_name is None:
            last_name_input = str(input("Please enter your last name: "))
            if validate_last_name(last_name_input):
                last_name = last_name_input
            else:
                continue
        if date_of_birth is None:
            date_of_birth_input = input("Please enter your date of birth (dd/mm/yyy): ")
            if validate_date_of_birth(date_of_birth_input):
                date_of_birth = date_of_birth_input
            else:
                continue
        if phone_number is None:
            phone_number_input = input("Please enter your phone number: ")
            if validate_phone_number(phone_number_input):
                phone_number = phone_number_input
            else:
                continue
        if address is None:
            address_input = input("Please enter your address: ")
            if validate_address(address_input):
                address = address_input
            else:
                continue

        break

    user = [email, password, role]
    create_user(user)

    admin_detail = [email, first_name, last_name, date_of_birth, phone_number, address]
    create_admin(admin_detail)