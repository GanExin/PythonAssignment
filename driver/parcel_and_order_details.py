from PythonAssignment.auth.validation.admin_validation import validate_date
from PythonAssignment.database import display_order, update_parcel_details, display_available_order

def update_parcel_status(session):
    current_user = session[0] #match driver email with current user

    delivery_status_available = ["Undelivered", "En route", "Delivered"]
    while True:
        try:
            print("\n---------------------Available orders---------------------")
            print(display_available_order())

            order_id_input = int(input("Enter Order ID: "))
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

                    update_parcel_details(order_id_input, new_status, new_date, new_driver)

                    updated_order = display_order(order_id_input)
                    print("\n---------------------Updated Order---------------------")
                    print(updated_order)
                    break

                if choice_to_deliver_order == "n":
                    break

        except ValueError:
            print("Invalid input. Please enter valid Order ID")