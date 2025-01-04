from PythonAssignment.auth.login import login
from PythonAssignment.auth.register import register

#Start page for users
def main():
    while True:
        print("\n#GROUP 20 \n#TP080733, TP080993, TP081103")
        choice = input("\nWelcome to Ship2Go, please select the following option: \n[1] Login \n[2] Register \n[3] Exit: ")
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