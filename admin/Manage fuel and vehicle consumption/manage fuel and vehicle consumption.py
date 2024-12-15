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
                    "FuelLevel": float(parts[2]),  # Fuel level as a float
                    "TotalFuelConsumed": float(parts[3]),  # Total fuel consumed as a float
                    "LastFuelCheck": parts[4]  # Date of last fuel check
                })
            else:
                pass
    return vehicles


def save_vehicle_data(filename, vehicles):
    """Save updated vehicle data to the text file."""
    with open(filename, "w") as file:
        for vehicle in vehicles:
            file.write(
                f"{vehicle['VehicleID']} | {vehicle['Model']} | {vehicle['FuelLevel']} | {vehicle['TotalFuelConsumed']} | {vehicle['LastFuelCheck']}\n"
            )


def view_fuel_data(vehicles):
    """Display fuel data for all vehicles."""
    print("\nVehicle Fuel Data:")
    print(f"{'ID':<5} {'Model':<15} {'Fuel Level':<12} {'Fuel Consumed':<15} {'Last Fuel Check':<15}")
    print("-" * 60)
    for vehicle in vehicles:
        print(
            f"{vehicle['VehicleID']:<5} {vehicle['Model']:<15} "
            f"{vehicle['FuelLevel']:<12} {vehicle['TotalFuelConsumed']:<15} {vehicle['LastFuelCheck']:<15}"
        )


def edit_fuel_data(vehicles, filename):
    """Edit fuel data for a specific vehicle."""
    vehicle_id = input("Enter the Vehicle ID to edit: ")
    for vehicle in vehicles:
        if vehicle["VehicleID"] == vehicle_id:
            print(f"Editing details for Vehicle {vehicle['VehicleID']} ({vehicle['Model']})")
            try:
                new_fuel_level = float(input(f"Enter new Fuel Level (current: {vehicle['FuelLevel']}): "))
                new_total_fuel_consumed = float(
                    input(f"Enter new Total Fuel Consumed (current: {vehicle['TotalFuelConsumed']}): ")
                )
                new_last_fuel_check = input(f"Enter new Last Fuel Check (current: {vehicle['LastFuelCheck']}): ")

                vehicle["FuelLevel"] = new_fuel_level
                vehicle["TotalFuelConsumed"] = new_total_fuel_consumed
                vehicle["LastFuelCheck"] = new_last_fuel_check

                save_vehicle_data(filename, vehicles)
                print("Vehicle data updated successfully!")
                return
            except ValueError:
                print("Invalid input. Please enter correct data.")
                return
    print(f"Vehicle with ID {vehicle_id} not found.")


def track_fuel_consumption(vehicles):
    """Track fuel consumption patterns for a specific vehicle."""
    print("\nAvailable Vehicles:")
    for idx, vehicle in enumerate(vehicles, start=1):
        print(f"{idx}. {vehicle['Model']}")

    try:
        choice = int(input("\nSelect a vehicle by number to track fuel consumption: "))
        if 1 <= choice <= len(vehicles):
            vehicle = vehicles[choice - 1]
            print(f"\nTracking fuel consumption for Vehicle {vehicle['VehicleID']} ({vehicle['Model']})")

            fuel_start = float(input(f"Enter starting fuel level (current: {vehicle['FuelLevel']}): "))
            fuel_end = float(input("Enter ending fuel level: "))
            route_used = input("Enter route used (e.g., Route 1, Route 2): ")

            if fuel_start < fuel_end:
                print("Error: Ending fuel level cannot be greater than the starting fuel level.")
                return

            total_fuel_consumed = fuel_start - fuel_end
            print(f"\nFuel Consumption Summary for Vehicle {vehicle['VehicleID']} ({vehicle['Model']}):")
            print(f"  Fuel Start Journey: {fuel_start} liters")
            print(f"  Fuel End Journey: {fuel_end} liters")
            print(f"  Total Fuel Consumed: {total_fuel_consumed} liters")
            print(f"  Route Used: {route_used}")
            print("-" * 40)

        else:
            print("Invalid choice. Please select a valid vehicle number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def maintenance_alerts(vehicles, threshold):
    """Display maintenance alerts if fuel consumption exceeds a certain threshold."""
    print("\nFuel Consumption Alerts:")
    for vehicle in vehicles:
        if vehicle["FuelLevel"] < threshold:
            print(f"Warning! Vehicle {vehicle['VehicleID']} ({vehicle['Model']}) has low fuel level ({vehicle['FuelLevel']} liters).")
        else:
            print(f"Vehicle {vehicle['VehicleID']} ({vehicle['Model']}) has sufficient fuel level ({vehicle['FuelLevel']} liters).")

def main():
    filename = "fuel_data.txt"
    vehicles = load_vehicle_data(filename)

    while True:
        print("\n--- Fuel & Vehicle Consumption Management ---")
        print("1. View Vehicle Fuel Data")
        print("2. Edit Vehicle Fuel Data")
        print("3. Track Fuel Consumption Patterns")
        print("4. Maintenance Alerts for Low Fuel")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_fuel_data(vehicles)
        elif choice == "2":
            edit_fuel_data(vehicles, filename)
        elif choice == "3":
            track_fuel_consumption(vehicles)
        elif choice == "4":
            threshold = float(input("Enter fuel level threshold (e.g., 10.0): "))
            maintenance_alerts(vehicles, threshold)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()