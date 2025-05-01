import csv
from data import storage
from views import ride_log


def show_add_ride():
    """Displays the Add Ride page and prompts user to select upload option."""
    print()
    print('='*40)
    print("|            ➕ ADD RIDE                |")
    print('='*40)
    print()
    print('How would you like to enter ride data?')
    print('[1] 🧑‍💻 Enter Ride Manually')
    print('[2] 📁 Upload Ride(s) via CSV file')
    print('[3] 🔙 Return to Ride Log')
    print()
    entry_choice = input('Key Option and Press Enter: ')

    if entry_choice == '1':
        manual_upload()
    elif entry_choice == '2':
        csv_upload()
    elif entry_choice == '3':
        ride_log.show_ride_log()


def manual_upload():
    """
    Prompts the user to manually enter ride details and then saves or
    cancels that entry.
    """
    print()
    print('*'*40)
    print('Enter the following ride elements below:')
    print('Date, Type, Distance, Time Elevation')
    print('Gain, and Location to save your ride.')
    print('*'*40)
    print()
    date = input('Enter Ride Date (MM-DD-YY): ')
    type = input('Enter Ride Type (Road, MTB, Trainer): ')
    distance = float(input('Enter Distance (mi): '))
    time = float(input('Enter Ride Time (min): '))
    elevation = input('Enter Elevation Gain (ft): ')
    location = input('Enter Ride Location (City): ')
    note = input('Enter Ride Note: ')
    print()
    print('Select an Option:')
    print('[1] ✅ Save Ride & Return to Ride Log')
    print('[2] ❌ Cancel & Return to Ride Log')
    print('[3] ❓ Help')

    user_choice = input("Key option and press Enter: ")

    if user_choice == '1':
        calculated_avg_speed = calculate_avg_speed(distance, time)
        ride = {
            'id': generate_id(),
            'date': date,
            'type': type,
            'distance': distance,
            'time': time,
            'average_speed': calculated_avg_speed,
            'elevation': elevation,
            'location': location,
            'note': [note]
        }

        rides = storage.load_rides()
        rides.append(ride)
        storage.save_rides(rides)
        print()
        print("✅ Ride Saved Successfully!")

        # Return to Ride Log
        ride_log.show_ride_log()

    if user_choice == '2':
        print()
        print("❌ Ride Entry Cancelled.")


def csv_upload():
    """
    Prompts the user to enter the path of a CSV file, then saves the
    ride stored in that file or prints an exception.
    """
    path = input("📁 Enter the path to CSV file: ")
    try:
        with open(path, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            rides = storage.load_rides()
            next_id = max((r['id'] for r in rides), default=0) + 1
            count = 0
            for row in reader:
                distance = float(row['distance'])
                time = float(row['time'])
                avg_speed = calculate_avg_speed(distance, time)
                ride = {
                    'id': next_id,
                    'date': row['date'],
                    'type': row['type'],
                    'distance': float(row['distance']),
                    'time': float(row['time']),
                    'average_speed': avg_speed,
                    'elevation': row['elevation'],
                    'location': row['location'],
                    'note': [row.get('note', "")]
                }
                rides.append(ride)
                next_id += 1
                count += 1

            storage.save_rides(rides)
            print('Reading File...')
            print()
            print('✅ Ride(s) imported successfully')

    except Exception as e:
        print(f"❌ Ride Import Failed: {e}")

    # Return to Ride Log page
    ride_log.show_ride_log()


def generate_id():
    """Generates the ride ID for a manually entered ride."""
    rides = storage.load_rides()
    if not rides:
        return 1
    return max(r['id'] for r in rides) + 1


def calculate_avg_speed(distance, time):
    """
    Takes as parameters distance (mi) and time (min) floats.
    Calulates and returns the average speed of the ride in mph.
    """
    time_hrs = time / 60
    avg_speed = distance / time_hrs
    return avg_speed
