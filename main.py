from PythonAssignment.auth.login import login
from PythonAssignment.auth.register import register


def main():
    while True:
        choice = input("Welcome to Ship2Go, please select the following option: [1] Login, [2] Register, [3] Exit: ")
        if choice == "1":
            success = login()
            if not success:
                print("Login Failed: Invalid Credentials")
        if choice == "2":
            register()
        if choice == "3":
            print("Thank you for using X App, see you again!")
            break
        else:
            print("Invalid option, please choose between [1], [2], or [3].")
            continue

main()