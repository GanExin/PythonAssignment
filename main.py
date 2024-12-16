from PythonAssignment.auth.login import login
from PythonAssignment.auth.register import register

#Start page for users
def main():
    while True:
        choice = input("Welcome to Ship2Go, please select the following option: [1] Login, [2] Register, [3] Exit: ")
        if choice == "1":
            success = login() #bring users to login()
            if not success:
                print("Login Failed: Invalid Credentials")
        if choice == "2":
            register() #bring users to register()
        if choice == "3":
            print("Thank you for using Ship2Go, see you again!") #Code ends
            break

main()