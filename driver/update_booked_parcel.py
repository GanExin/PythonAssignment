from PythonAssignment.auth.validation.admin_validation import validate_date
from PythonAssignment.database import display_driver_jobs, display_order, update_parcel_details


def update_booked_parcel_details(session):
    current_user = session[0]  # matching current email
    print(f"Fetching orders for driver: {current_user}...\n")
    orders = display_driver_jobs(current_user)

    if orders == f"No jobs found for driver: {current_user}": #check if user booked orders
        print("No orders found. Please book available parcels first.")
        return

    print("\n---------------------Driver Orders---------------------")
    print(orders)

    while True:
        delivery_status_available = ["Undelivered", "En route", "Delivered"]

        choice = input("Would you like to update a parcel?(y/n): ").lower()
        if choice == "y":
            while True:
                order_id_input = input("Please enter the Order ID you want to update: ")
                order_found = display_order(order_id_input)
                if order_found :
                    if f"Driver: {current_user}" in order_found:
                        print("\n---------------------Order found---------------------")
                        print(order_found)

                        while True:
                            choice_to_update_order = input("\nWould you like to update this order? (y/n): ").lower()
                            if choice_to_update_order == "y":
                                while True:
                                    new_status = input("Enter new delivery status [Undelivered/En route/Delivered]: ").capitalize()
                                    if new_status not in delivery_status_available:
                                        print("Invalid input. Please try again.")
                                        continue
                                    while True:
                                        new_date = input("Enter new date(dd/mm/yyyy): ")
                                        if not validate_date(new_date):
                                            continue
                                        break
                                    break

                                update_parcel_details(order_id_input, new_status, new_date, current_user)

                                updated_order = display_order(order_id_input)
                                print("\n---------------------Updated Order---------------------")
                                print(updated_order)
                                return

                            elif choice_to_update_order == "n":
                                break
                    else:
                        print(f"Order ID {order_id_input} is booked by another driver.")
                else:
                    print("Order ID not found.")

        elif choice == "n":
            break
