from data import storage
import zmq
import json
from views import home


def show_stats():
    """Displays the user's lifetime cycling statistics page."""
    print()
    print('='*40)
    print("|        📊 LIFETIME STATISTICS        |")
    print('='*40)
    print()
    get_stats()
    print()
    print('Select an Option:')
    print()
    print('[1]: 🏠 Return Home')
    print('[9]: 🚪 Exit')
    print()
    user_choice_handler()


def get_stats():
    """
    Requests the user's lifetime cycling statistics by sending the user's
    ride data to the cycling statistics microservice via ZEROMQ. Receives
    the statistics and prints them to the console.
    """
    rides = storage.load_rides()

    # Create context and socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4321")

    # Send ride data in JSON format
    socket.send_json(rides)

    # Get response with stats
    message = socket.recv()
    stats_json_string = message.decode()

    # Convert JSON-formatted string to object
    stats_json = json.loads(stats_json_string)

    print(f"Total Ride Distance: {stats_json['total_ride_distance']} mi")
    print()
    print(f"Total Ride Time: {stats_json['total_ride_time']} mins")
    print()
    print(f"Overall Average Speed: {stats_json['overall_average_speed']} mph")
    print()
    print(f"Total Elevation Gain: {stats_json['total_elevation_gain']} ft")
    print()
    print(f"Average Ride Distance: {stats_json['average_ride_distance']} mi")
    print()
    print(f"Average Elevation Gain: {stats_json['average_elevation_gain']} ft")

    # Tell server to quit
    socket.send_string("Q")


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
