from PythonAssignment.auth.validation.driver_validation import validate_driver_email, validate_driver_password


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
    email = None
    password = None
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
        break

    print("Successfully Registered Account! Email: " + email + " Password: " + password)


    # password = input("Please enter password: ")
    # first_name = str(input("Please enter first name: "))
    # last_name = str(input("Please enter last name: "))
    # phone_number = int(input("Please enter phone number: "))
    # address = input("Please enter your address: ")
    # availability_status = input("")

def register_admin():
    print("admin registration")