from PythonAssignment.database import read_users, read_driver_details


def update_delivery_details(session):
    users = read_users()
    current_user = session[0]

    driver = read_driver_details(current_user)

    for user in users:
        db_email = user[0]
        if current_user == db_email:
            while True:
                choice = input("Please select a number to update? "
                               "\n[1]Vehicle ID \n[2] Route Chosen \n[3]Start journey details \n[4]End journey details"
                               "\n[5] Turnaround time \n[6]No. of refills \n[7]No. of stopovers \n[8]Current fuel level "
                               "\n[9]Total cost of fuel \n[10]Safety & cleaning status"
                               "\n[11]exit: ")

                if choice == "1":
                    pass
                if choice == "2":
                    pass
                if choice == "3":
                    pass
                if choice == "4":
                    pass
                if choice == "5":
                    pass
                if choice == "6":
                    pass
                if choice == "7":
                    pass
                if choice == "8":
                    pass
                if choice == "9":
                    pass
                if choice == "10":
                    pass
                if choice == "11":
                    return