from PythonAssignment.database import display_driver_details

def driver_management(session):
    print("---------------------Driver Management---------------------")
    # Admin chooses from the driver management features
    while True:
        choice = input("[1] View Driver Detail \n[2] Add Comment to driver "
                       "\n[3] View Comment for drivers \n[4] Exit "
                       "\nPlease choose a feature (1/2/3/4): ")

        if choice == '1':
            view_driver_details(session)
        elif choice == '2':
            add_comment_to_driver(session)
        elif choice == '3':
            view_comment_for_drivers(session)
        elif choice == "4":
            print("Exiting Driver Management. Returning to main menu.")
            break
        else:
            print("Invalid input. Please choose a valid option.")

def view_driver_details(session):
    print("---------------View Driver Details---------------")

    try:
        with open("./database_driver/driver_profile.txt", "r") as file:
            found = False #To check if we find any driver details
            for line in file:
                driver_data = line.strip().split(" | ") #remove extra spaces and split the line by " | "
                driver_details = display_driver_details(driver_data) # Call the function
                print("\nDriver Details:")
                print(driver_details)
                print("----------------------------------------")
                found = True #set the found flag to true after driver details found

            if not found:
                print("No driver profiles found.")
    except FileNotFoundError:
        print("No driver profile found. Please ensure the driver profile exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def add_comment_to_driver(session):
    print("---------------Add Comment to Driver---------------")
    driver_email = input("Please enter the driver's email: ").strip() #Ask user to enter driver's email and remove extra space

    try:
        with open("./database_driver/driver_profile.txt", "r") as file: #open driver profile in read mode
            driver_found = False # To check if driver is found
            driver_name = "" # Placeholder to store driver's name
            for line in file:
                driver_data = line.strip().split(" | ")
                if driver_data[0] == driver_email: #check if driver's email matches the one user input
                    driver_name = f"{driver_data[1]} {driver_data[2]}"
                    driver_found = True # Set to true after driver is found
                    break #Exit loop

            if not driver_found:
                print("Driver not found. Please check the email and try again.")
                return

        comment = input("Please enter your comment: ").strip() #Add comment to driver

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
            if content: #check if file have content
                print("\n---------------All Driver Comments---------------")
                print(content)
            else:
                print("\nNo comments available yet.")
    except FileNotFoundError:
        print("No driver comments found. Please ensure the comments file exists.")


















