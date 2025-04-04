from PythonAssignment.database import store_rate_review
from PythonAssignment.customer.user_order_management import place_order

def rate_review(session):
    print("---------------------Ratings & Reviews---------------------")
    # asks users if they had placed and order or not
    order_made = input("Have you made an order? (y/n): ").lower()

    while True:
        if order_made == "n": # if user has not made an order, bring them to place order menu
            print("Please ensure you have made an order to rate and review.")
            place_order(session)
            break
        elif order_made == "y": # if user has placed an order, they can:
            user = input("Please enter your full name: ") # enter their name
            while True:
                # give a rating of 1-5 stars
                rating = int(input("How many ⭐ would you give to rate the service (1-5): "))

                if 1 <= rating <= 5: # make sure users enter a number from 1-5
                    # clarify/shows users how many stars they gave
                    print(f"You rated {rating}⭐ for the service. Rating complete.")
                    break
                else: # if user enters a number out of range, reprompt to let them rate again.
                    print("Please enter a number between 1 and 5.")

            # user enters their review
            review = input("Please leave a review regarding the services provided: ")
            print("Review complete.") # let users know their review is completed
            print("Thank you for rating and reviewing.")

            review_from_user = [user, rating, review]
            store_rate_review(review_from_user)
            # store the details in .txt file

            display_reviews() # displays the reviews other users have made

            break
        else:
            print("Invalid choice. Please try again.")
            order_made = input("Have you made an order? (y/n): ").lower()

# function that displays the other reviews
def display_reviews():
    try:
        with open("./database_customer/user_rate_review.txt", "r") as file:
            content = file.read()
            if content:
                print("\n---------------------All Ratings & Reviews---------------------")
                print(content)  # Display the content of the file
            else:
                print("\nNo reviews available yet.")
    except FileNotFoundError:
        print("No reviews found.")


