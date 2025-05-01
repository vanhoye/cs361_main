from data import storage
from views import ride_log, home


def show_delete_ride(ride_id):
    """
    Takes as a parameter the ride id of the ride to be deleted.
    Displays the Delete Ride page and deletes or cancels the deletion
    of the ride.
    """
    print()
    print('='*40)
    print("|           🗑️ DELETE RIDE            |")
    print('='*40)
    print()
    print("You're about to delete the following ride:")
    print()

    # Load rides and select ride with designated id.
    rides = storage.load_rides()
    ride = next((r for r in rides if str(r['id']) == str(ride_id)), None)

    # If ride with designated id not found.
    if not ride:
        print(f"❌ Ride with ID: {ride['id']} not found.")
        user_choice_handler()

    else:
        print(f" ID:                {ride['id']}")
        print(f" Date:              {ride['date']}")
        print(f" Type:              {ride['type']}")
        print(f" Distance (mi):     {ride['distance']}")
        print(f" Time (min):        {ride['time']}")
        print(f" Elevation (ft):    {ride['elevation']}")
        print(f" Location (City):   {ride['location']}")
        print(f" Note:              {ride['note']}")
        print()

        print("❗️PLEASE NOTE: RIDE DATA WILL BE PERMANENTLY DELETED❗️")
        print("❗️THIS ACTION CANNOT BE UNDONE❗️")
        print()
        confirm = input("Are you sure you want to delete this ride? (yes/no): ")

        if confirm == 'yes':
            # Delete ride from list of rides.
            rides.remove(ride)
            # Save updated list of rides.
            storage.save_rides(rides)
            print()
            print(f"🗑️ Ride ID: {ride['id']} deleted successfully.")
            print()
            user_choice_handler()
        elif confirm == 'no':
            print()
            print(f"❌ Ride ID: {ride['id']} has not been deleted.")
            user_choice_handler()
        else:
            print("❗️ Invalid entry. Please type yes or no.")


def user_choice_handler():
    """Displays and interprets user options on the Delete Ride page."""
    print('Select an Option')
    print('[1] 🗒️ Return to Ride Log')
    print('[2] 🏠 Return Home')
    print()
    user_choice = input('Key option and press Enter: ')

    if user_choice == '1':
        ride_log.show_ride_log()
    elif user_choice == '2':
        home.show_home()
    else:
        print("'❗️ Error: Invalid choice. Please try again.'")
