from PythonAssignment.auth.validation.driver_validation import validate_driver_password
from PythonAssignment.database import read_users, update_password_to_db


def update_password(session):
    users = read_users()
    current_user = session[0]

    for user in users:
        db_email = user[0]
        if current_user == db_email:
            while True:
                new_password = input("Please input new password: ")

                if validate_driver_password(new_password):
                    user[1] = new_password
                    update_password_to_db(users)
                    print(f"Password updated for email: {user[0]} !")
                    return

    print("User email does not match.")

def update_profile(session):
    print("driver's details")
