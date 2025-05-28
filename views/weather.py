import zmq
import json
from views import home


def show_weather():
    """Displays the current weather for a given zip code."""
    print()
    print('='*40)
    print("|        ⛈️ CURRENT WEATHER        |")
    print('='*40)
    print()
    get_weather()
    print()
    print('Select an Option:')
    print()
    print('[1]: 🏠 Return Home')
    print('[9]: 🚪 Exit')
    print()
    user_choice_handler()


def get_weather():
    """
    Requests a given zip code's current weather conditions by sending
    a zip code to the weather checker microservice via ZEROMQ.
    Receives the zip code's name, temperature in F, conditions, wind
    speed in MPH, and humdity and prints them to the console.
    """

    # Create context and socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5566")

    zip_code = input("Enter ZIP code: ")
    socket.send_string(zip_code)

    response = socket.recv_string()

    # Convert JSON-formatted string to object
    weather_data = json.loads(response)
    print()
    print(f"Location: {weather_data['location']}")
    print()
    print(f"Temperature: {weather_data['temperature']} F")
    print()
    print(f"Conditions: {weather_data['conditions']}")
    print()
    print(f"Wind Speed: {weather_data['wind_speed']} mph")
    print()
    print(f"Humidity: {weather_data['humidity']}%")


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
