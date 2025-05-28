import pyfiglet
from rich.console import Console
from views import add_ride, ride_log, help, stats, weather, export_rides


def show_home():
    """
    Displays the home page and prompts the user to navigate the
    application.
    """
    console = Console()
    print()
    print('='*65)
    home_banner = pyfiglet.figlet_format("CycleTracker", font="slant")
    console.print(home_banner, style='blue')
    print('='*65)
    print()
    print('*'*65)
    print("""Record your completed rides to track your cycling progress!""")
    print('*'*65)
    print()
    print('HOME')
    print('-'*40)
    print('Select an Option:')
    print('[1]: ➕  Add a Ride')
    print('[2]: 🗒️  View Ride Log')
    print('[3]: ❓  Help')
    print('[4]: 📊  View Liftime Stats')
    print('[5]: ⛈️  View Weather')
    print('[6]: 💾  Export Rides to CSV')
    print('[9]: 🚪  Exit')
    print()

    # Provide user with app navigation options.
    user_choice_handler()


def user_choice_handler():
    """Provide user with app navigation options."""
    selection = input('Key option and press Enter: ')
    if selection == '1':
        add_ride.show_add_ride()
    elif selection == '2':
        ride_log.show_ride_log()
    elif selection == '3':
        help.show_help()
    elif selection == '4':
        stats.show_stats()
    elif selection == '5':
        weather.show_weather()
    elif selection == '6':
        export_rides.show_export_rides()
    elif selection == '9':
        print('\n👋 Thank you for using CycleTracker. See you next ride!')
        print()
    else:
        print('❗️ Error: Invalid choice. Please try again.')
