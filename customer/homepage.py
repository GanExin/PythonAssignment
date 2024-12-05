from PythonAssignment.customer.rating_and_reviews import rate_review
from PythonAssignment.customer.user_order_management import order_management


def customer_homepage(session):

    print("Welcome back!")

    while True:
        user_choice = int(input("[1] Manage orders \n[2] Rate and Review \nWhat would you like to do?: "))

        if user_choice == 1:
            order_management(session)
        elif user_choice == 2:
            rate_review(session)
        else:
            print("Invalid choice. Please choose either [1] or [2]")
            continue