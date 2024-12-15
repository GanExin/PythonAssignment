def convert_to_hours(time_str):
    """Convert a time string (e.g., '4 hours') to a float representing hours."""
    return float(time_str.split()[0])


def calculate_turnaround_time(route_details, stopover_time):
    """Calculate the total turnaround time for a route."""
    total_travel_time = sum(convert_to_hours(part['time']) for part in route_details)
    total_stopover_time = convert_to_hours(stopover_time) * len(route_details)
    return total_travel_time + total_stopover_time


def calculate_fuel_consumption(route_details, fuel_rate):
    """Calculate the fuel consumption for a route based on travel time and fuel rate."""
    total_travel_time = sum(convert_to_hours(part['time']) for part in route_details)
    return total_travel_time * fuel_rate


def calculate_estimated_delivery_time(route_details, stopover_time):
    """Calculate the estimated delivery time for a route."""
    return calculate_turnaround_time(route_details, stopover_time)


def display_route_details(route_details):
    """Display the route details in the desired format."""
    for part in route_details:
        print(f"{part['from']} -> {part['to']}: {part['time']}")


def process_trip_data(filename, driver_email, route_choice, route_details, stopover_time, fuel_rate, turnaround_time,
                      fuel_consumption, estimated_delivery_time):
    """Save the trip details to a file."""
    with open(filename, 'a') as file:
        file.write(f"Driver: {driver_email}\n")
        file.write(f"Route chosen: {route_choice}\n")
        file.write(f"Route details:\n")
        for part in route_details:
            file.write(f"{part['from']} -> {part['to']}: {part['time']}\n")
        file.write(f"Stopover time: {stopover_time}\n")
        file.write(f"Fuel consumption per hour: {fuel_rate} liters\n")
        file.write(f"Turnaround time: {turnaround_time:.2f} hours\n")
        file.write(f"Fuel consumption: {fuel_consumption:.2f} liters\n")
        file.write(f"Estimated delivery time: {estimated_delivery_time:.2f} hours\n")
        file.write("\n" + "-" * 30 + "\n")


def main():
    """Main function to execute the program."""
    # Get driver's email
    driver_email = input("Enter your email: ")

    # Display available routes
    print("\nAvailable Routes:")
    print("1. Route 1: Johor -> Kuala Lumpur -> Butterworth -> Kedah -> Perlis")
    print("2. Route 2: Johor -> Kuala Lumpur -> Terengganu -> Kelantan")

    # Ask driver to choose a route
    route_choice = input("Choose a route (1 for Route 1, 2 for Route 2): ")

    if route_choice == "1":
        route_choice = "Route 1"
        route_details = [
            {'from': 'Johor', 'to': 'Kuala Lumpur', 'time': '4 hours'},
            {'from': 'Kuala Lumpur', 'to': 'Butterworth', 'time': '3 hours'},
            {'from': 'Butterworth', 'to': 'Kedah', 'time': '2 hours'},
            {'from': 'Kedah', 'to': 'Perlis', 'time': '1 hour'}
        ]
        stopover_time = "0.5 hours"
        fuel_rate = 8  # liters per hour
    elif route_choice == "2":
        route_choice = "Route 2"
        route_details = [
            {'from': 'Johor', 'to': 'Kuala Lumpur', 'time': '4 hours'},
            {'from': 'Kuala Lumpur', 'to': 'Terengganu', 'time': '5 hours'},
            {'from': 'Terengganu', 'to': 'Kelantan', 'time': '3 hours'}
        ]
        stopover_time = "0.5 hours"
        fuel_rate = 10  # liters per hour
    else:
        print("Invalid choice. Exiting program.")
        return

    # Calculate necessary values
    turnaround_time = calculate_turnaround_time(route_details, stopover_time)
    fuel_consumption = calculate_fuel_consumption(route_details, fuel_rate)
    estimated_delivery_time = calculate_estimated_delivery_time(route_details, stopover_time)

    # Display details
    print("\nDriver Details and Route Information:")
    print(f"Driver: {driver_email}")
    print(f"Route chosen: {route_choice}")

    print("\nRoute details:")
    display_route_details(route_details)

    print(f"\nStopover time: {stopover_time}")
    print(f"Fuel consumption per hour: {fuel_rate} liters")
    print(f"Turnaround time: {turnaround_time:.2f} hours")
    print(f"Fuel consumption: {fuel_consumption:.2f} liters")
    print(f"Estimated delivery time: {estimated_delivery_time:.2f} hours")

    # Save the details to a text file
    filename = "trip_details.txt"
    process_trip_data(filename, driver_email, route_choice, route_details, stopover_time, fuel_rate, turnaround_time,
                      fuel_consumption, estimated_delivery_time)
    print("\nDetails saved to trip_details.txt")


if __name__ == '__main__':
    main()
