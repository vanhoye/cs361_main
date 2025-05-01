from data import storage
from views import ride_details


def show_add_note(ride_id):
    """Displays the Add Note page and prompts the user to add a new note."""
    print()
    print('='*40)
    print("|           📝 ADD NOTE           |")
    print('='*40)
    print()

    # Load rides and select ride with designated id.
    rides = storage.load_rides()
    ride = next((r for r in rides if str(r['id']) == str(ride_id)), None)

    print("You're adding a note to:")
    print(f"Ride ID: {ride['id']}")
    print(f"Date: {ride['date']}")
    print()
    print('Existing Note:')
    print(f"{ride['note']}")
    print()
    print("Type additional note below. Press Enter when done: ")
    new_note = input()

    # Add new note to ride and save record.
    ride['note'].append(new_note)
    storage.save_rides(rides)
    print()

    # Provide user with app navigation options.
    print('Select an Option:')
    print('[1] 📝 Add another Note')
    print('[2] 🔍 Return to Ride Details')
    print()
    user_choice = input("Key option and press Enter: ")

    if user_choice == '1':
        show_add_note(ride_id)
    elif user_choice == '2':
        ride_details.show_ride_details(ride_id)
    else:
        print('❗️ Error: Invalid choice. Please try again.')
