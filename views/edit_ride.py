from data import storage
from views import ride_details
from views import add_ride


def show_edit_ride(ride_id):
    """
    Takes as a parameter the ride id of the ride to have a note added.
    Displays the Edit Ride page and prompts the user to edit ride elements.
    Then prompts user to save or cancel the changes.
    """
    print()
    print('='*40)
    print("|           ✎ EDIT RIDE            |")
    print('='*40)
    print()

    # Load rides and select ride with designated id.
    rides = storage.load_rides()
    ride = next((r for r in rides if str(r['id']) == str(ride_id)), None)

    # Display which ride is being edited.
    print(f"Editing Ride ID: {ride['id']}")

    print('*'*40)
    print('When prompted, enter new data or press')
    print('Enter to keep the current value.')
    print('*'*40)
    print()

    # Prompt user to edit ride elements.
    print(f"Date: {ride['date']}")
    new_date = input('New Date (MM-DD-YY): ')
    print()
    if new_date != '':
        ride['date'] = new_date

    print(f"Type: {ride['type']}")
    new_type = input('New type (Road, MTB, Trainer): ')
    print()
    if new_type != '':
        ride['type'] = new_type

    print(f"Distance (mi): {ride['distance']}")
    new_distance = (input('New Distance (mi): '))
    print()
    if new_distance != '':
        ride['distance'] = float(new_distance)

    print(f"Time (min): {ride['time']}")
    new_time = (input('New Time (min): '))
    print()
    if new_time != '':
        ride['time'] = float(new_time)

    print(f"Elevation (ft): {ride['elevation']}")
    new_elevation = input('New Elevation Gain (ft): ')
    print()
    if new_elevation != '':
        ride['elevation'] = new_elevation

    print(f"Location (City): {ride['location']}")
    new_location = input('New Location (City): ')
    print()
    if new_location != '':
        ride['location'] = new_location

    print(f"Note: {ride['note']}")
    new_note = input('New Note: ')
    print()
    if new_note != '':
        ride['note'] = new_note

    # Prompt user to Save or Cancel edit changes.
    print()
    print('Select an Option:')
    print('[1] ✅ Save Changes')
    print('[2] ❌ Cancel and Return to Ride Details')
    print()
    user_choice = input('Key option and press Enter: ')

    if user_choice == '1':
        new_avg_speed = add_ride.calculate_avg_speed(ride['distance'], ride['time'])
        ride['average_speed'] = new_avg_speed
        storage.save_rides(rides)
        print(f"✅ Ride ID: {ride['id']} updated successfully!")
        ride_details.show_ride_details(ride_id)

    elif user_choice == '2':
        print('❌ Changes cancelled')
        ride_details.show_ride_details(ride_id)

    else:
        print('❗️ Error: Invalid choice. Please try again.')
