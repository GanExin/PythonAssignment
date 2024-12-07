# Order Management (let user choose a feature)

from PythonAssignment.database import next_order_id, create_order


def order_management(session):
    print("---------------------Order Management---------------------")
    # user enters a number (1-7) to choose what feature they want
    while True:
        choice = input("[1] Place Order \n[2] Track Order "
                       "\n[3] Monitor Order \n[4] Cancel Order \n[5] Reorder \n[6] View Order History"
                       "\n[7] Exit"
                       "\nPlease choose a feature (1/2/3/4/5/6/7): ")
        if choice == '1':
            place_order(session)
        elif choice == '2':
            track_order(session)
        elif choice == '3':
            monitor_order(session)
        elif choice == '4':
            pass #cancel_order(session)
        elif choice == '5':
            reorder(session)
        elif choice == '6':
            pass #view_order_history
        elif choice == '7':
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
                   customer_phone_num, user_payment_choice, vehicle, user_special_request]
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
        with open("database_customer/orders.txt", "r") as file:
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

# Monitor order
def monitor_order(session):
    print("-----------------------Monitor Order-----------------------")
    user_orderid = int(input("Please enter your Order ID: ")) # user enters orderID

    try:
        with open("database_customer/orders.txt", "r") as file: # reads orders.txt file for the orderID
            lines = file.readlines()
        current_order_id = None
        order_found = False
        for line in lines:
            line = line.strip()
            if line.startswith("Order ID:"):
                current_order_id = int(line.split(":")[1].strip())
                if current_order_id == user_orderid:
                    order_found = True
                    break
        if order_found:
            while True:
                user_package_received = input("Have you received your order? (y/n): ").lower()
                if user_package_received == "y":
                    print("You have received your package. Thank you for using Ship2Go!")
                    break
                elif user_package_received == "n":
                    pass
                    break
                else:
                    print("Invalid Choice. Please try again.")
        else:
            print("Order ID not found. Please try again.")
    except FileNotFoundError:
        print("No orders found. Please ensure you have placed an order.")

# Cancel order


# Reorder
def reorder(session):
    print("-----------------------Reorder-----------------------")
    order_id = int(input("Please enter your Order ID: "))

    try:
        with open("database_customer/orders.txt", "r") as file:
            lines = file.readlines()
        current_order_id = None
        for line in lines:
            line = line.strip()
            if line.startswith("Order ID:"):
                current_order_id = int(line.split(":")[1].strip())
                if current_order_id == order_id:
                    print(f"Order found. Reordering Successful")
                    return
        print("Order ID not found. Reorder unsuccessful.")
    except FileNotFoundError:
        print("No previous orders found. Please ensure you have placed an order.")

# View order history
