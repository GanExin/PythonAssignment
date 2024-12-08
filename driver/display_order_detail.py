from PythonAssignment.database import find_order_by_id, display_order


def prompt_for_order_id(session):
    current_user = session[0]

    orders = display_order()  #display all order details
    while True:
        try:
            order_id_input = int(input("Enter Order ID: "))
            order_found = find_order_by_id(order_id_input, orders) #check if order exist, if it does, print order details
            if order_found:
                print("\n---------------------Order found---------------------")
                for key, value in order_found.items():
                    print(f"{key}: {value}")
                break  # Exit the loop if the order is found
            else:
                print("Order ID not found. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid Order ID.")