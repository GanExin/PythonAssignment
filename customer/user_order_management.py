# Order Management (let user choose a feature)

from PythonAssignment.database import next_order_id, create_order


def order_management(session):
    print("---------------------Order Management---------------------")
    # user enters a number (1-7) to choose what feature they want
    while True:
        choice = input("[1] Place Order \n[2] Track Order "
                       "\n[3] Cancel Order \n[4] Reorder \n[5] View Order History"
                       "\n[6] Exit"
                       "\nPlease choose a feature (1/2/3/4/5/6): ")
        if choice == '1':
            place_order(session)
        elif choice == '2':
            track_order(session)
        elif choice == '3':
            cancel_order(session)
        elif choice == '4':
            reorder(session)
        elif choice == '5':
            view_order_history(session)
        elif choice == '6':
            print("Thank you for using Ship2Go.")
            break
        else:
            print("Invalid input")


# Place order
def place_order(session):

    order_id = next_order_id()

    print("-----------------------Place Order-----------------------")
    print("Please enter the following details.") # user enters the following details for the order
    product_name = input("Product Name: ")
    product_quantity = int(input("Quantity: "))
    customer_name = input("Full Name: ")
    customer_address = input("Address: ")
    customer_phone_num = input("Phone Number: ")
    delivery_status = "Undelivered"
    status_update_date = "NIL"

    # a list of payment methods users can choose from
    payment_method = ["Cash on Delivery", "Debit Card", "Credit Card", "Bank Transfer"]
    # user inputs the payment method they prefer
    while True:
        user_payment_choice = input("Please enter a payment method\n[Cash on Delivery] \n[Debit Card] \n"
                                    "[Credit Card] \n[Bank Transfer] :")
        # user's payment method will be rejected if the method is not mentioned in the payment_method list.
        if user_payment_choice not in payment_method:
            print("Invalid choice. Please try again.")
        # clarify/shows users the payment method they have chosen.
        else:
            print(f"You have chosen {user_payment_choice}")
            break

    # a list of consignment sizes
    consignment_sizes = ["small parcel", "bulk order", "special cargo"]
    # a list of vehicle choices
    vehicle_choices = ["Van", "Truck", "Specialized Carrier"]
    vehicle = "" # set vehicle to blank
    # user inputs their consignment size
    while True:
        user_consignment_sizes = input("Enter the consignment size of your delivery"
                                       " (small parcel/bulk order/special cargo): ").strip().lower()
        if user_consignment_sizes not in consignment_sizes:
            print("Invalid Choice. Please try again.")
        else:
            if user_consignment_sizes == "small parcel":
                vehicle = vehicle_choices[0]
            elif user_consignment_sizes == "bulk order":
                vehicle = vehicle_choices[1]
            else:
                vehicle = vehicle_choices[2]
            break
    print(f"Your assigned vehicle is: {vehicle}")

    user_special_request = None
    while True:
        special_requests = input("Would you like to make any special requests for your order? (y/n): ")
        if special_requests == "n":
            print("No special requests made.")
            break
        elif special_requests == "y":
            user_special_request = input("What is your special request?: ")
            print("Special requests made.")
            break
        else:
            print("Invalid choice. Please try again.")
    # shows users their orderID
    print(f"Order successful, your OrderID is {order_id}.")


    # Save order details in .txt
    save_order = [order_id, product_name, product_quantity, customer_name, customer_address,
                   customer_phone_num, user_payment_choice, vehicle, user_special_request, delivery_status, status_update_date]
    create_order(save_order)

    # asks users if they want to place another order
    order_again = input("Would you like to place another order? (y/n): ").lower()
    if order_again == "y":  # if yes, bring them back to the place order menu
        place_order(session)
    else:
        print("Thank you for ordering.\n")


# Track order
def track_order(session):
    print("-----------------------Track Order-----------------------")
    # User enters their orderID to track that specific order
    order_id = input("Please enter your Order ID: ")
    try:
        with open("./database_customer/orders.txt", "r") as file:
            found = False
            order_details = ""
            for line in file:
                # Check if the current line contains the entered Order ID
                if line.strip() == f"Order ID: {order_id}":
                    found = True
                    order_details += line
                    while True:
                        line = file.readline()
                        if not line or line.startswith("-" * 40):
                            break
                        order_details += line
                    break
            if found:
                print("\nOrder Details:")
                print(order_details) # displays the order details of the specific orderID entered by user
            else:
                print("Order not found. Please check your Order ID.")
    except FileNotFoundError:
        print("No orders found. Please ensure you have placed an order.")


# Cancel order
def cancel_order(session):
    print("-----------------------Cancel Order-----------------------")
    order_id = int(input("Please enter your Order ID: "))
    try:
        with open("./database_customer/orders.txt", "r") as file:
            found = False
            order_details = ""
            for line in file:
                # Check if the current line contains the entered Order ID
                if line.strip() == f"Order ID: {order_id}":
                    found = True
                    order_details += line
                    while True:
                        line = file.readline()
                        if not line or line.startswith("-" * 40):
                            break
                        order_details += line
                    break
            if found:
                delivery_status = ""
                for detail_line in order_details.split("\n"):
                    if "Delivery status:" in detail_line:
                        delivery_status = detail_line.split("Delivery status:")[1].strip()
                        print(f"Delivery Status: {delivery_status}")
                        break
                if delivery_status == "Delivered":
                    print("Cannot cancel delivered orders. Cancellation unsuccessful.")
                elif delivery_status in ["En route", "Undelivered"]:
                    cancel_confirmation = input("Order cancellation confirmed? (y/n): ").lower()
                    while True:
                        if cancel_confirmation == "":
                            print("Please enter yes or no (y/n).")
                            cancel_confirmation = input("Order cancellation confirmed? (y/n): ").lower()
                        elif cancel_confirmation == "y":
                            order_cancellation(order_id)
                            break
                        else:
                            print("Order cancellation unsuccessful.")
                            break
            else:
                print("Order not found. Please check your Order ID.")
    except FileNotFoundError:
        print("No orders found. Please ensure you have placed an order.")

def order_cancellation(order_id):
    try:
        with open("./database_customer/orders.txt", "r") as file:
            orders = file.read()
        # Split the file into blocks of orders
        order_blocks = orders.split("----------------------------------------\n")
        updated_orders = []
        found = False
        for block in order_blocks:
            if block.strip() and f"Order ID: {order_id}" in block:
                found = True
            else:
                updated_orders.append(block)
        if found:
            with open("./database_customer/orders.txt", "w") as file:
                file.write("----------------------------------------\n".join(updated_orders).strip() + "\n")
            print("Order cancellation complete.")
        else:
            print("Order not found. Please check your Order ID.")
    except FileNotFoundError:
        print("Orders file not found. Please ensure the file exists.")


# Reorder
def reorder(session):
    print("-----------------------Reorder-----------------------")
    order_id = int(input("Please enter your Order ID: "))
    try:
        with open("./database_customer/orders.txt", "r") as file:
            lines = file.readlines()
        current_order_id = None
        order_details = []
        # Search for the order details
        for line in lines:
            line = line.strip()
            if line.startswith("Order ID:"):
                current_order_id = int(line.split(":")[1].strip())
            if current_order_id == order_id:
                order_details.append(line)
            if line == '----------------------------------------' and current_order_id == order_id:
                break
        if order_details:
            # Get the next order ID using the next_order_id function
            new_order_id = next_order_id()
            # Open the file in append mode to add the new order
            with open("./database_customer/orders.txt", "a") as file:
                for i, detail in enumerate(order_details):
                    if detail.startswith("Order ID:"):
                        order_details[i] = f"Order ID: {new_order_id}"
                file.writelines("\n".join(order_details))
            print(f"Order found. Reordering Successful. Your new Order ID is: {new_order_id}")
            print("\nReorder Details:" )
            print("\n".join(order_details))
        else:
            print("Order ID not found. Reorder unsuccessful.")
    except FileNotFoundError:
        print("No previous orders found. Please ensure you have placed an order.")


# View order history
def search_orders_by_name(file_path, customer_name):
    try:
        with open("./database_customer/orders.txt", "r") as file:
            content = file.read()  # Read the entire file content
        orders = content.split("\n----------------------------------------\n")
        found = False
        # Loops through each order and check if the customer's name matches
        for order in orders:
            if f"Customer Name: {customer_name}" in order:
                print("\nMatching Order:")
                print(order.strip())  # Print the full order
                print("-" * 40)
                found = True
        if not found:
            print(f"No orders found for Customer Name: {customer_name}.")
    except FileNotFoundError:
        print("Please ensure you have placed an order.")

def view_order_history(session):
    print("-----------------------View Order History-----------------------")
    while True:
        customer_name = input("Enter your name: ").strip()
        if search_orders_by_name("./database_customer/orders.txt", customer_name):
            break
        else:
            pass