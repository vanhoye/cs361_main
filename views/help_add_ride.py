from views import help


def show_help_add_ride():
    """Prints step by step instructions on how to add a ride."""
    print('='*40)
    print("|        ➕ HOW TO ADD A RIDE          |")
    print('='*40)
    print()

    print("A ride can be added two ways:")
    print("🧑‍💻 Manual Entry:")
    print("The program will prompt you to enter:")
    print("-Ride Date (MM-DD-YY)")
    print("-Ride Type (Road, MTB, Trainer)")
    print("-Distance (mi)")
    print("-Ride Time (min)")
    print("-Elevation Gain (ft)")
    print("-Ride Location (City)")
    print()

    print("📁 Upload via CSV File")
    print("-When prompted, select the path to a CSV File with Ride Data")
    print("-CSV File must include headers: date, type, distance, time, elevation, location, note")
    print()

    # Return to help menu
    user_choice = input("Press Enter to return to Help Menu: ")
    if user_choice == '':
        help.show_help()
    else:
        print("'❗️ Error: Invalid choice. Please try again.'")
