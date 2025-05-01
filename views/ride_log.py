from data import storage
from views import ride_details, add_ride, help, home
from tabulate import tabulate


def show_ride_log():
    """Displays the ride log page. Displays list of Rides with their date,
    type, distance, and time in table format."""
    print()
    print('='*40)
    print("|              🗒️ RIDE LOG              |")
    print('='*40)
    print()

    rides = storage.load_rides()

    # If the user has not added any rides yet.
    if not rides:
        print("❗️You have not added any rides yet❗️")
        print()
        user_choice_handler()
        return

    table = [
        [r['id'], r['date'], r['type'], r['distance'], r['time']]
        for r in rides
    ]

    headers = ["ID", "Date", "Type", "Distance (mi)", "Duration (min)"]

    print()
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

    print()
    user_choice_handler()


def user_choice_handler():
    """Displays and interprets user options on the Ride Log page."""
    print('What would you like to do?')
    print('[1] 🔍 View Ride Details')
    print('[2] ➕ Add a Ride')
    print('[3] ❓ Help')
    print('[4] 🏠 Return Home')
    print()
    user_choice = input('Key option and press Enter: ')

    if user_choice == '1':
        print()
        ride_choice = input('To view ride details, enter Ride ID: ')
        ride_details.show_ride_details(ride_choice)
    elif user_choice == '2':
        add_ride.show_add_ride()
    elif user_choice == '3':
        help.show_help()
    elif user_choice == '4':
        home.show_home()
    else:
        print("'❗️ Error: Invalid choice. Please try again.'")
