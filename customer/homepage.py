from PythonAssignment.customer.rating_and_reviews import rate_review
from PythonAssignment.customer.user_order_management import order_management
from PythonAssignment.database import read_customer_details, read_users


def customer_homepage(session):
    profile = read_customer_details(session[0])
    users = read_users()

    print("Welcome back! " + profile[1] + "!")

    while True:
        user_choice = input("[1] Manage orders \n[2] Rate and Review \n"
                            "[3] Exit \nWhat would you like to do?: ")

        if user_choice == "1":
            order_management(session)
        if user_choice == "2":
            rate_review(session)
        if user_choice == "3":
            break