import zmq
from data import storage
from tabulate import tabulate
from views import ride_log, ride_details, home

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6000")


def show_sorted_ride_log():
    """
    Displays the sorted ride log page. Prompts the user to input which
    parameter they want to sort by, and whether they want to sort in ascending
    or descending order. Sends this request via ZEROMQ to sort ride log
    microservice. Receives the ride data sorted by the given parameter
    and displays them in a table.
    """
    print()
    print('='*40)
    print("|          🔼 SORTED RIDE LOG          |")
    print('='*40)
    print()

    rides = storage.load_rides()

    # If the user has not added any rides yet.
    if not rides:
        print("❗️You have not added any rides yet❗️")
        print()
        user_choice_handler()
        return

    parameter = input("Which parameter would you like to sort by ('date', 'distance', or 'time')?: ")
    ascending = input("Enter 'True' for Ascending or 'False' for Descending sort direction: ")

    request = {
        "ride_data": rides,
        "sort_by": parameter,
        "ascending": ascending
    }

    socket.send_json(request)

    response = socket.recv_json()

    table = [
        [r['id'], r['date'], r['type'], r['distance'], r['time']]
        for r in response
    ]

    headers = ["ID", "Date", "Type", "Distance (mi)", "Time (min)"]

    print()
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    print()
    user_choice_handler()


def user_choice_handler():
    """Displays and interprets user options on the Ride Log page."""
    print('What would you like to do?')
    print('[1] 🔍 View Ride Details')
    print('[2] 🗒️ Return to Ride Log')
    print('[3] 🏠 Return Home')
    print()
    user_choice = input('Key option and press Enter: ')

    if user_choice == '1':
        print()
        ride_choice = input('To view ride details, enter Ride ID: ')
        ride_details.show_ride_details(ride_choice)
    elif user_choice == '2':
        ride_log.show_ride_log()
    elif user_choice == '3':
        home.show_home()
    else:
        print("'❗️ Error: Invalid choice. Please try again.'")
