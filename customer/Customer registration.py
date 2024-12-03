#register new customer
def customer_registration():
    print("---------------------Customer Registration---------------------")
    print("Welcome, please enter the details below and register to Ship2GO.\n")
customer_registration()

#registration details/validity/store_data_in_database
def registration_details_validity():
    customer_information = {}

#full name
    while True:
        full_name = input("Full Name: ")  # customer inputs full name
        formatted_name = full_name.title()

        if full_name == "":  # to check whether full name is empty
            print("Full Name cannot be empty. Please try Again")
        elif full_name != formatted_name:  # to check if first letter of each name is capitalized
            print("First letter of each name must be capitalized. Please try Again.")
        else:  # name is valid, store name in customer_data.txt
            customer_information["full_name"] = formatted_name
            break

#email address
    # read emails in customer_data.txt to check if emails already exists
    def is_email_in_use(email, filename="customer_data.txt"):
        with open(filename, "r") as file:
            for line in file:
                if email in line:
                    return True
        return False

    while True:
        email_address = input("Email Address: ")  # customer inputs email

        if email_address == "":  # check whether email is empty
            print("Email Address cannot be empty. Please try again.")
        elif "@" not in email_address or "." not in email_address:  # check if email contains @ and .
            print("Email Address must contain '@' and '.' Please try again.")
        elif is_email_in_use(email_address):  # check if email is already in customer_data.txt
            print("This email has already been used. Please try again.")
        else:  # email is valid, store email in customer_data.txt
            customer_information["email"] = email_address.strip()
            break

#phone num
    def is_phone_in_use(phone, filename="customer_data.txt"):
        with open(filename, "r") as file:
            for line in file:
                if phone in line:
                    return True
        return False

    while True:
        phone_num = input("Phone Number: ")
        if phone_num == "":
            print("Phone Number cannot be empty. Please try again.")
        elif "-" not in phone_num:
            print("Phone Number must contain '-'. Please try again.")
        elif is_phone_in_use(phone_num):
            print("This Phone Number has already been used. Please try again.")
        else:
            customer_information["phone_num"] = phone_num.strip()
            break

#address
    while True:
        address = input("Address: ")
        if address.strip():
            customer_information["address"] = address.strip()
            break
        else:
            print("Address Cannot be empty. Please try again.")

    save_to_file(customer_information)
    return customer_information

'''def save_to_file(customer_info_file):
    with open("customer_data.txt", "a") as file:
        file.write(f"Full Name: {customer_info_file['full_name']}\n")
        file.write(f"Email Address: {customer_info_file['email']}\n")
        file.write(f"Phone Number: {customer_info_file['phone_num']}\n")
        file.write(f"Address: {customer_info_file['address']}\n")
        file.write("-" * 40 + "\n")
    print("\n⭐You have successfully registered⭐")'''

# customer_info = registration_details_validity()

def save_to_file(customer_info_file):
    with open("customer_data.txt", "a") as file:
        file.write(f"{customer_info_file['full_name']} | {customer_info_file['email']} | "
                   f"{customer_info_file['phone_num']} | {customer_info_file['address']}\n")
    print("\n⭐You have successfully registered⭐")

customer_info = registration_details_validity()