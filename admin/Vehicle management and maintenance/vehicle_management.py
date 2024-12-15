def load_vehicle_data(filename):
    """Load vehicle data from the text file."""
    vehicles = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts) == 5:  # Ensure the line has exactly 5 fields
                vehicles.append({
                    "VehicleID": parts[0],
                    "Model": parts[1],
                    "LastInspection": parts[2],
                    "Performance": parts[3],
                    "MaintenanceHistory": parts[4]
                })
            else:
                pass
    return vehicles


def view_vehicle_data(vehicles):
    """Display all vehicle data."""
    print("\nVehicle Data:")
    print(f"{'ID':<5} {'Model':<15} {'Last Inspection':<15} {'Performance':<10}")
    print("-" * 50)
    for vehicle in vehicles:
        print(
            f"{vehicle['VehicleID']:<5} {vehicle['Model']:<15} "
            f"{vehicle['LastInspection']:<15} {vehicle['Performance']:<10}"
        )

def view_maintenance_history(vehicles):
    """Display maintenance history for each vehicle."""
    print("\nMaintenance History:")
    for vehicle in vehicles:
        print(f"\nVehicle {vehicle['VehicleID']} - {vehicle['Model']}:")
        history = vehicle["MaintenanceHistory"].split(";")
        for record in history:
            if ":" in record:  # Check if the record contains a colon
                date, task = record.split(":")
                print(f"  {date} - {task}")
            else:
                print(f"  Invalid record: {record}")


def maintenance_alerts(vehicles, current_date):
    """Display maintenance alerts based on inspection dates."""
    print("\nMaintenance Alerts:")
    for vehicle in vehicles:
        if vehicle["LastInspection"] < current_date:
            print(
                f"Vehicle {vehicle['VehicleID']} ({vehicle['Model']}) needs maintenance! "
                f"Last inspection date: {vehicle['LastInspection']}."
            )
        else:
            print(
                f"Vehicle {vehicle['VehicleID']} ({vehicle['Model']}) is up-to-date. "
                f"Last inspection date: {vehicle['LastInspection']}."
            )

def main():
    filename = "vehicles.txt"
    vehicles = load_vehicle_data(filename)

    while True:
        print("\n--- Vehicle Management System ---")
        print("1. View Vehicle Data")
        print("2. View Maintenance History")
        print("3. Maintenance Alerts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_vehicle_data(vehicles)
        elif choice == "2":
            view_maintenance_history(vehicles)
        elif choice == "3":
            current_date = input("Enter current date (YYYY-MM-DD): ")
            maintenance_alerts(vehicles, current_date)
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
