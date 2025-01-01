from PythonAssignment.auth.validation.driver_validation import validate_email, \
    validate_route_chosen, validate_date_time, validate_number, \
    validate_float_with_two_decimals, validate_yes_or_no
from PythonAssignment.database import read_users, read_driver_details, display_driver_jobs, \
    create_delivery_details, read_delivery_details, display_delivery_details, \
    update_route_to_db, update_s_journey_date_time_to_db, update_e_journey_date_time_to_db, \
    update_turnaround_time_to_db, update_total_distance_to_db, update_total_refuel_to_db, update_total_stopover_to_db, \
    update_current_fuel_level_to_db, update_total_cost_of_refuel_to_db, update_safety_cleaning_status_to_db, \
    update_current_location_to_db, update_total_fuel_consumption_to_db, check_driver_parcel


def delivery_details(session):
    users = read_users()
    current_user = session[0]  # match driver email with current user

    if not check_driver_parcel(current_user):
        print("You have not booked a parcel yet. Please book a parcel first.")
        return

    while True:
        view_jobs_or_update_input = input("\nWould you like to: \n[1]view all your booked jobs"
                                                  "\n[2]update current delivery details"
                                                  "\n[3]create new delivery details"
                                                  "\n[4]exit: ")
        if view_jobs_or_update_input == "1":
            view_driver_orders(session)
        elif view_jobs_or_update_input == "2":
            update_delivery_details(session)
        elif view_jobs_or_update_input == "3":
            create_new_delivery_detail(session)
        elif view_jobs_or_update_input == "4":
            break
        else:
            continue
        break


def view_driver_orders(session):
    current_user = session[0]  #matching current email
    print(f"Fetching orders for driver: {current_user}...\n")
    orders = display_driver_jobs(current_user)
    print("\n---------------------Driver Orders---------------------")
    print(orders)

def create_new_delivery_detail(session):
    users = read_users()
    current_user = session[0]

    for user in users:
        db_email = user[0]
        if current_user == db_email:
            detail = read_delivery_details(current_user)

            if detail:
                print(f"{current_user} already created details. Please update instead.")
                return

            if not detail:
                print("\n---------------------New delivery details---------------------\n")
                print("Welcome, please enter the details below to create new delivery details.\n")

                current_location_choices = ["Johor","Kuala Lumpur", "Butterworth", "Terengganu", "Kelantan", "Perlis"]

                email = current_user
                route = None
                s_journey_date_time = None
                e_journey_date_time = None
                turnaround_time = None
                current_location = None
                total_distance_travelled = None
                total_refuel = None
                total_stopover = None
                current_fuel_level = None
                total_cost_of_fuel_refill = None
                safety_cleaning_check = None
                fuel_consumption = None
                while True:
                    if route is None:
                        route_input = input("Available routes:"
                                            "\nRoute 1: Johor ➜ Kuala Lumpur ➜ Butterworth ➜ Kedah ➜ Perlis"
                                            "\nRoute 2: Johor ➜ Kuala Lumpur ➜ Terengganu ➜ Kelantan"
                                            "\nPlease enter chosen route [1/2]: ")
                        if validate_route_chosen(route_input):
                            route = route_input
                        else:
                            continue
                    if s_journey_date_time is None:
                        s_journey_date_time_input = input("Please START of journey date and time (dd/mm/yyy; hh:mm) : ")
                        if validate_date_time(s_journey_date_time_input):
                            s_journey_date_time = s_journey_date_time_input
                        else:
                            continue
                    if e_journey_date_time is None:
                        e_journey_date_time_input = input("Please END of journey date and time (dd/mm/yyy; hh:mm) "
                                                          "or 'NIL' (if driver is still 'en route'): ")
                        if validate_date_time(e_journey_date_time_input) or e_journey_date_time_input == "NIL":
                            e_journey_date_time = e_journey_date_time_input
                        else:
                            continue
                    if turnaround_time is None:
                        turnaround_time_input = input("Please total turnaround time (total duration of trip in hours): ")
                        if validate_number(turnaround_time_input):
                            turnaround_time = turnaround_time_input
                        else:
                            continue
                    if current_location is None:
                        current_location_input = input("Choice = [Johor], [Kuala Lumpur], [Butterworth], [Terengganu], [Kelantan], [Perlis]"
                                                       "\nPlease enter your current location: ")
                        if current_location_input in current_location_choices:
                            current_location = current_location_input
                        else:
                            continue
                    if total_distance_travelled is None:
                        total_distance_travelled_input =input("Please enter total distance travelled (in km): ")
                        if validate_number(total_distance_travelled_input):
                            total_distance_travelled = total_distance_travelled_input
                        else:
                            continue
                    if total_refuel is None:
                        total_refuel_input = input("Please enter total number of refuels you had from the whole journey: ")
                        if validate_number(total_refuel_input):
                            total_refuel = total_refuel_input
                        else:
                            continue
                    if total_stopover is None:
                        total_stopover_input = input("Please enter total stopovers you had from the whole journey: ")
                        if validate_number(total_stopover_input):
                            total_stopover = total_stopover_input
                        else:
                            continue
                    if current_fuel_level is None:
                        current_fuel_level_input = input("Please enter current fuel level (%): ")
                        if validate_number(current_fuel_level_input):
                            current_fuel_level = current_fuel_level_input
                        else:
                            continue
                    if total_cost_of_fuel_refill is None:
                        total_cost_of_fuel_refill_input = input("Please enter total cost of fuel refills in RM(2 decimal places): ")
                        if validate_float_with_two_decimals(total_cost_of_fuel_refill_input):
                            total_cost_of_fuel_refill = total_cost_of_fuel_refill_input
                        else:
                            continue
                    if safety_cleaning_check is None:
                        safety_cleaning_check_input = input("Have you conduct safety and cleaning check on your journey? (y/n): ").lower()
                        if validate_yes_or_no(safety_cleaning_check_input):
                            safety_cleaning_check = safety_cleaning_check_input
                        else:
                            continue
                    if fuel_consumption is None:
                        fuel_consumption_input = input("Please enter how much fuel you have consumed (in litres): ")
                        if validate_number(fuel_consumption_input):
                            fuel_consumption_total = str(int(fuel_consumption_input)/ int(total_distance_travelled))
                            fuel_consumption = fuel_consumption_total
                        else:
                            continue

                    break

                new_delivery_details = [email, route, s_journey_date_time, e_journey_date_time, turnaround_time,
                                        current_location, total_distance_travelled, total_refuel, total_stopover, current_fuel_level,
                                        total_cost_of_fuel_refill, safety_cleaning_check, fuel_consumption]
                create_delivery_details(new_delivery_details)

def update_delivery_details(session):
    users = read_users()
    current_user = session[0]

    for user in users:
        db_email = user[0]
        if current_user == db_email:
            detail = read_delivery_details(current_user)

            if not detail:
                print(f"No delivery details found for {current_user}. Please create new details.")
                return

            if detail:
                while True:
                    current_details = display_delivery_details(detail)
                    print("\n---------------------Current delivery details---------------------\n")
                    print(current_details)

                    choice_to_update = input("\nWould you like to update your details? (y/n): ").lower()

                    if choice_to_update == "y":

                        current_location_choices = ["Johor", "Kuala Lumpur", "Butterworth", "Terengganu",
                                                    "Kelantan", "Perlis"]

                        print("\n---------------------Update delivery details---------------------\n")
                        choice = input("Please select a number to update? "
                                       "\n[1]Route Chosen \n[2]Start journey details \n[3]End journey details"
                                       "\n[4]Turnaround time \n[5]Driver current location \n[6]Total distance travelled"
                                       " and fuel consumed \n[7]Total refuels \n[8]Total stopovers "
                                       "\n[9]Current fuel level \n[10]Total cost of fuel "
                                       "\n[11]Safety & cleaning status \n[12]exit: ")

                        if choice == "1":
                            update_route_chosen = input(f"Your current chosen route is route {detail[1]}. "
                                                        f"\nAvailable routes:"
                                                        f"\nRoute 1: Johor ➜ Kuala Lumpur ➜ Butterworth ➜ Kedah ➜ Perlis"
                                                        f"\nRoute 2: Johor ➜ Kuala Lumpur ➜ Terengganu ➜ Kelantan"
                                                        f"\nPlease enter new route [1/2]: ")
                            if validate_route_chosen(update_route_chosen):
                                detail[1] = update_route_chosen
                                update_route_to_db(detail)
                                print(f"\n⭐Route {detail[1]} successfully updated for email: {user[0]} !⭐ \n")
                                print(display_delivery_details(detail))

                        elif choice == "2":
                            update_s_journey_datetime = input(f"Your current START journey date; time is {detail[2]}."
                                                              f"\nPlease enter new (dd/mm/yyyy; hh:mm) : ")
                            if validate_date_time(update_s_journey_datetime):
                                detail[2] = update_s_journey_datetime
                                update_s_journey_date_time_to_db(detail)
                                print(f"\n⭐{detail[2]} successfully updated for email: {user[0]} !⭐ \n")
                                print(display_delivery_details(detail))

                        elif choice == "3":
                            update_e_journey_datetime = input(f"Your current END journey date; time is {detail[3]}."
                                                              f"\nPlease enter new (dd/mm/yyyy; hh:mm) "
                                                              f"or 'NIL' (if driver is still 'en route'): ")
                            if validate_date_time(update_e_journey_datetime) or update_e_journey_datetime == "NIL":
                                detail[3] = update_e_journey_datetime
                                update_e_journey_date_time_to_db(detail)
                                print(f"\n⭐{detail[3]} successfully updated for email: {user[0]} !⭐ \n")
                                print(display_delivery_details(detail))

                        elif choice == "4":
                            update_turnaround_time = input(f"Your current turnaround time is {detail[4]} hours."
                                                           f"\nPlease enter new turnaround time (in hours): ")
                            if validate_number(update_turnaround_time):
                                detail[4] = update_turnaround_time
                                update_turnaround_time_to_db(detail)
                                print(f"\n⭐{detail[4]} hours successfully updated for email: {user[0]} !⭐ \n")
                                print(display_delivery_details(detail))

                        elif choice == "5":
                            update_current_location = input(f"Your current location is {detail[5]}."
                                                            f"\nChoice = [Johor], [Kuala Lumpur], [Butterworth], [Terengganu], [Kelantan], [Perlis]"
                                                            f"\nPlease enter new current location:")
                            if update_current_location in current_location_choices:
                                detail[5] = update_current_location
                                update_current_location_to_db(detail)
                                print(f"\n⭐{detail[5]} successfully updated for email: {user[0]} !⭐ \n")
                                print(display_delivery_details(detail))

                        elif choice == "6":
                            update_total_distance_travelled = input(f"Your current distance travelled is {detail[6]} km."
                                                                    f"\nPlease enter new distance travelled (in km): ")
                            if validate_number(update_total_distance_travelled):
                                detail[6] = update_total_distance_travelled
                                update_total_distance_to_db(detail)
                                if update_total_distance_travelled:
                                    fuel_consumption_input = input(
                                        "Please enter how much fuel you have consumed (in litres): ")
                                    if validate_number(fuel_consumption_input):
                                        update_fuel_consumption_total = str(int(fuel_consumption_input) / int(
                                            update_total_distance_travelled))
                                        detail[12] = update_fuel_consumption_total
                                        update_total_fuel_consumption_to_db(detail)

                                print(f"\n⭐{detail[6]} km  and total fuel consumption of {detail[12]} litres"
                                      f"successfully updated for email: {user[0]} !⭐ \n")
                                print(display_delivery_details(detail))

                        elif choice == "7":
                            update_total_refuels = input(f"Your current total refuel is {detail[7]}."
                                                         f"\nPlease enter new total refuel: ")
                            if validate_number(update_total_refuels):
                                detail[7] = update_total_refuels
                                update_total_refuel_to_db(detail)
                                print(f"\n⭐{detail[7]} successfully updated for email: {user[0]} !⭐ \n")
                                print(display_delivery_details(detail))

                        elif choice == "8":
                            update_total_stopovers = input(f"Your current total stopover is {detail[8]} times. "
                                                           f"\nPlease enter new total stopover: ")
                            if validate_number(update_total_stopovers):
                                detail[8] = update_total_stopovers
                                update_total_stopover_to_db(detail)
                                print(f"\n⭐{detail[8]} times successfully updated for email: {user[0]} !⭐ \n")
                                print(display_delivery_details(detail))

                        elif choice == "9":
                            update_current_fuel_level = input(f"Your current fuel level is {detail[9]}%. "
                                                              f"\nPlease enter new fuel level (in %): ")
                            if validate_number(update_current_fuel_level):
                                detail[9] = update_current_fuel_level
                                update_current_fuel_level_to_db(detail)
                                print(f"\n⭐{detail[9]}% successfully updated for email: {user[0]} !⭐ \n")
                                print(display_delivery_details(detail))

                        elif choice == "10":
                            update_total_cost_refuel = input(f"Your current cost of refuel is RM{detail[10]}. "
                                                             f"\nPlease enter new cost of refuel [RM(2 decimal places)]: ")
                            if validate_number(update_total_cost_refuel):
                                detail[10] = update_total_cost_refuel
                                update_total_cost_of_refuel_to_db(detail)
                                print(f"\n⭐RM{detail[10]} successfully updated for email: {user[0]} !⭐ \n")
                                print(display_delivery_details(detail))

                        elif choice == "11":
                            update_safety_cleaning_check = input(f"Your current safety and cleaning check status is {detail[11]}."
                                                                 f"\nPlease enter new status [y/n]: ")
                            if validate_yes_or_no(update_safety_cleaning_check):
                                detail[11] = update_safety_cleaning_check
                                update_safety_cleaning_status_to_db(detail)
                                print(f"\n⭐{detail[11]} successfully updated for email: {user[0]} !⭐ \n")
                                print(display_delivery_details(detail))

                        elif choice == "12":
                            return

                    if choice_to_update == "n":
                        break
