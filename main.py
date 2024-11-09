from PythonAssignment.auth.login import login
from PythonAssignment.auth.register import register


def main():
    while True:
        choice = input("Welcome to X App, please select the following option: [1] Login, [2] Register, [3] Exit: ")
        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Thank you for using X App, see you again!")
            break
        else:
            print("Invalid option")
            continue

main()