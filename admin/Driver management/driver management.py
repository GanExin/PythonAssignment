def load_drivers(filename):
    drivers = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts) == 5:  # Ensure all required fields are present
                try:
                    drivers.append({
                        "Email": parts[0],
                        "Name": parts[1].split(": ")[1],
                        "Status": parts[2].split(": ")[1],
                        "VehicleID": parts[3].split(": ")[1],
                        "Location": parts[4].split(": ")[1],
                    })
                except IndexError:
                    pass
            else:
                pass
    return drivers

def save_drivers(filename, drivers):
    with open(filename, 'w') as file:
        for driver in drivers:
            file.write(
                f"{driver['Email']} | name: {driver['Name']} | status: {driver['Status']} | vehicle: {driver['VehicleID']} | location: {driver['Location']}\n"
            )

def view_drivers(drivers):
    print("Email               | Name         | Status       | Vehicle | Location")
    print("---------------------------------------------------------------------")
    for driver in drivers:
        print(
            f"{driver['Email']} | {driver['Name']} | {driver['Status']} | {driver['VehicleID']} | {driver['Location']}"
        )

def comment_to_driver(drivers):
    email = input("Enter the driver's email to comment on: ")
    for driver in drivers:
        if driver["Email"] == email:
            print(f"Driver: {driver['Name']} (Current Status: {driver['Status']})")
            comment = input("Enter your comment: ")
            driver["Status"] += f" ({comment})"
            print("Comment added successfully.")
            return
    print("Driver not found.")

def main():
    filename = "driver_data.txt"
    drivers = load_drivers(filename)

    while True:
        print("\nDriver Management Menu")
        print("1. View Drivers")
        print("2. Comment to Driver")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_drivers(drivers)
        elif choice == "2":
            comment_to_driver(drivers)
            save_drivers(filename, drivers)
        elif choice == "3":
            print("Exiting Driver Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()