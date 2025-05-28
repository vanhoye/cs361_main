import zmq
from data import storage
from views import home


def show_export_rides():
    """Displays the export rides to csv page."""
    print()
    print('='*40)
    print("|        💾 EXPORT RIDES TO CSV        |")
    print('='*40)
    print()
    print("Do you want to export your ride data to a CSV file?")
    decision = input("Type 'yes' or 'no': ")
    print()
    if decision == 'yes':
        export_rides()
    print()
    print('Select an Option:')
    print()
    print('[1]: 🏠 Return Home')
    print('[9]: 🚪 Exit')
    print()
    user_choice_handler()


def export_rides():
    """
    Sends the application's ride data stored in rides.json to the export
    to CSV microservice via ZEROMQ. Receives a string indicating the filepath
    where the CSV file was saved.
    """
    # Create context and socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:6001")

    # Load and send rides
    rides = storage.load_rides()
    socket.send_json(rides)

    # Receive and print file path where CSV file saved
    file_path = socket.recv_string()
    print(file_path)


def user_choice_handler():
    """Provide user with app navigation options."""
    selection = input('Key option and press Enter: ')
    if selection == '1':
        home.show_home()
    elif selection == '9':
        print('\n👋 Thank you for using CycleTracker. See you next ride!')
        print()
    else:
        print('❗️ Error: Invalid choice. Please try again.')
