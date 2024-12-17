from PythonAssignment.auth.validation.admin_validation import validate_date
from PythonAssignment.database import display_order, update_delivery_status_and_date


def update_parcel_status(session):
    current_user = session[0] #display all order details

    delivery_status_available = ["Undelivered", "En route", "Delivered"]
    while True:
        try:
            order_id_input = int(input("Enter Order ID: "))
            order_found = display_order(order_id_input)  # check if order exist, if it does, print order details
            if order_found:
                print("\n---------------------Order found---------------------")
                print(order_found)

                choice_to_update = input("\nWould you like to update Delivery status and date? (y/n): ").lower()
                if choice_to_update == "y":
                    new_status = input("Enter new delivery status [Undelivered/En route/Delivered]: ").capitalize()
                    if new_status not in delivery_status_available:
                        print("Invalid input. Please try again.")
                        continue
                    new_date = input("Enter new date(dd/mm/yyyy): ")
                    if not validate_date(new_date):
                        continue

                    update_delivery_status_and_date(order_id_input,new_status,new_date)

                    updated_order = display_order(order_id_input)
                    print("\n---------------------Updated Order---------------------")
                    print(updated_order)
                    break

                if choice_to_update == "n":
                    break

        except ValueError:
            print("Invalid input. Please enter valid Order ID")