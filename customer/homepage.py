# how to import user_order_management py
def customer_homepage(session):
    print("Welcome back!")

    user_choice = int(input("[1] Manage orders \n[2] Rate and Review \nWhat would you like to do?: "))

    while True:
        if user_choice == 1:
            pass  # order_management()
        elif user_choice == 2:
            pass  # rate_review()
        else:
            print("Invalid choice. Please choose either [1] or [2]")
            user_choice = input("[1] Manage orders \n[2] Rate and Review \nWhat would you like to do?: ")