from PythonAssignment.auth.validation.admin_validation import validate_date
from PythonAssignment.database import display_order, update_parcel_details, display_available_order, \
    read_driver_details, read_users


def update_parcel_driver(session):
    users = read_users()
    current_user = session[0] #match driver email with current user

    drivers = read_driver_details(current_user)
    assigned_vehicle = drivers[9]

    delivery_status_available = ["Undelivered", "En route", "Delivered"]
    for user in users:
        db_email = user[0]
        if current_user == db_email:
            if assigned_vehicle and assigned_vehicle != "None":
                while True:
                    try:
                        print("\n---------------------Available orders---------------------")
                        available_orders, order_ids = display_available_order()
                        if available_orders == "No available orders found.":
                            print(available_orders)
                            break #if no available orders, break

                        print(available_orders) #if orders are available, print details

                        order_id_input = str(input("Please enter the Order ID you want to book: "))
                        if order_id_input not in order_ids:
                            print("Invalid Order ID. Please choose valid Order IDs from the displayed list.")
                            continue #prompt user to try again when order ID is invalid

                        order_found = display_order(order_id_input)  # check if order exist, if it does, print order details
                        if order_found:
                            print("\n---------------------Order found---------------------")
                            print(order_found)

                            choice_to_deliver_order = input("\nWould you like to take deliver this order? (y/n): ").lower()
                            if choice_to_deliver_order == "y":
                                new_driver = current_user
                                new_status = input("Enter new delivery status [Undelivered/En route/Delivered]: ").capitalize()
                                if new_status not in delivery_status_available:
                                    print("Invalid input. Please try again.")
                                    continue
                                new_date = input("Enter new date(dd/mm/yyyy): ")
                                if not validate_date(new_date):
                                    continue

                                update_parcel_details(str(order_id_input), new_status, new_date, new_driver)

                                updated_order = display_order(order_id_input)
                                print("\n---------------------Updated Order---------------------")
                                print(updated_order)
                                break

                            if choice_to_deliver_order == "n":
                                break

                    except ValueError:
                        print("\nInvalid input. Please enter valid Order ID")

            else:
                print("Unable to book parcels due to user not assigned a vehicle.")
                break