from PythonAssignment.database import display_driver_details

def driver_management(session):
    print("---------------------Driver Management---------------------")
    # Admin chooses from the driver management features
    while True:
        choice = input("[1] Add New Driver \n[2] View Driver Detail"
                       "\n[3] Add Comment to driver \n[4] View Comment for drivers "
                       "\n[5] Exit "
                       "\nPlease choose a feature (1/2/3/4/5): ")
        if choice == '1':
            add_new_driver(session)
        elif choice == '2':
            view_driver_details(session)
        elif choice == '3':
            add_comment_to_driver(session)
        elif choice == '4':
            view_comment_for_drivers(session)
        elif choice == "5":
            print("Exiting Driver Management. Returning to main menu.")
            break
        else:
            print("Invalid input. Please choose a valid option.")


def add_new_driver(session):
    print("---------------Add New Driver---------------")
    try:
        email = input("Enter the driver's email: ").strip()

        with open("./database_driver/driver_profile.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                driver_data = line.strip().split(" | ")
                if driver_data[0] == email:
                    print(f"The email {email} is already in use. Please enter a different email.")
                    return

        first_name = input("Enter the driver's first name: ").strip()
        last_name = input("Enter the driver's last name: ").strip()
        phone_number = input("Enter the driver's phone number: ").strip()
        address = input("Enter the driver's address: ").strip()
        availability_status = input("Enter the driver's availability status (available/unavailable): ").strip().lower()
        driver_license = input("Enter the driver's license number: ").strip()
        health_report = input("Enter the driver's health report (fit to drive/not fit to drive): ").strip().lower()
        family_dependencies = input("Enter the number of family dependencies: ").strip()

        new_driver = f"{email} | {first_name} | {last_name} | {phone_number} | {address} | {availability_status} | {driver_license} | {health_report} | {family_dependencies} | None\n"


        with open("./database_driver/driver_profile.txt", "a") as file:
            file.write(new_driver)

        print(f"New driver with email {email} added successfully.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_driver_details(session):
    print("---------------View Driver Details---------------")

    try:
        with open("./database_driver/driver_profile.txt", "r") as file:
            found = False
            for line in file:
                driver_data = line.strip().split(" | ")
                driver_details = display_driver_details(driver_data)
                print("\nDriver Details:")
                print(driver_details)
                print("----------------------------------------")
                found = True

            if not found:
                print("No driver profiles found.")
    except FileNotFoundError:
        print("No driver profile found. Please ensure the driver profile exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def add_comment_to_driver(session):
    print("---------------Add Comment to Driver---------------")
    driver_email = input("Please enter the driver's email: ")
    comment = input("Please enter your comment: ")

    try:

        with open("./database_driver/driver_profile.txt", "r") as file:
            driver_found = False
            for line in file:
                driver_data = line.strip().split(" | ")
                if driver_data[0] == driver_email:
                    driver_name = f"{driver_data[1]} {driver_data[2]}"
                    driver_found = True
                    break

            if not driver_found:
                print("Driver not found. Please check the email and try again.")
                return

        with open("./database_admin/driver_comment.txt", "a") as file:
            file.write(f"Name: {driver_name}\n")
            file.write(f"Email: {driver_email}\n")
            file.write(f"Comment: {comment}\n\n")
            file.write("----------------------------------------\n")

        print("Comment added successfully!")

    except FileNotFoundError:
        print("Driver profile or comments file not found. Please ensure the files exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def view_comment_for_drivers(session):
    try:
        with open("./database_admin/driver_comment.txt", "r") as file:
            content = file.read()
            if content:
                print("\n---------------All Driver Comments---------------")
                print(content)
            else:
                print("\nNo comments available yet.")
    except FileNotFoundError:
        print("No driver comments found. Please ensure the comments file exists.")


















