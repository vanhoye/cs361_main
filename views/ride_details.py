from data import storage
from views import edit_ride, delete_ride, ride_log, add_note, help


def show_ride_details(ride_id):
    """
    Takes as a parameter the ride id of the ride whose details are to
    be shown. Displays the Ride Details page and gives users the options
    to edit, delete, or add note to ride.
    """
    print()
    print('='*40)
    print("|           🔍 RIDE DETAILS            |")
    print('='*40)
    print()

    # Load rides and select ride with designated id.
    rides = storage.load_rides()
    ride = next((r for r in rides if str(r['id']) == str(ride_id)), None)

    # If ride with designated id not found.
    if not ride:
        print("❌ Ride not found.")
        return

    print(f" ID:                {ride['id']}")
    print(f" Date:              {ride['date']}")
    print(f" Type:              {ride['type']}")
    print(f" Distance (mi):     {ride['distance']}")
    print(f" Time (min):        {ride['time']}")
    print(f" Avg Speed (mph)    {ride['average_speed']:.2f}")
    print(f" Elevation (ft):    {ride['elevation']}")
    print(f" Location (City):   {ride['location']}")
    print(f" Note:              {ride['note']}")
    print()

    print('Select an Option:')
    print('[1] ✎ Edit Ride')
    print('[2] 🗑️ Delete Ride')
    print('[3] 📝 Add Note')
    print('[4] ❓ Help')
    print('[5] 🔙 Return to Ride Log')
    print()
    user_choice = input('Key option and press Enter: ')

    if user_choice == '1':
        edit_ride.show_edit_ride(ride_id)
    if user_choice == '2':
        delete_ride.show_delete_ride(ride_id)
    if user_choice == '3':
        add_note.show_add_note(ride_id)
    if user_choice == '4':
        help.show_help()
    if user_choice == '5':
        ride_log.show_ride_log()
