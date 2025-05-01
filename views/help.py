from views import help_add_ride, help_edit_ride, help_add_note, help_delete_ride, ride_log, home


def show_help():
    """
    Displays the Help Menu page and prompts the user to navigate to the
    various Help pages or return to the Ride Log or Ride Details pages.
    """
    print()
    print('='*40)
    print("|              ❓ HELP                 |")
    print('='*40)
    print()
    print('Select an Option:')
    print('[1] ➕ How to Add a Ride')
    print('[2] ✎ How to Edit a Ride')
    print('[3] 📝 How to Add a Note')
    print('[4] 🗑️ How to Delete a Ride')
    print('[5] 🗒️ View Ride Log')
    print('[6] 🏠 Return Home')
    print()
    user_choice_handler()


def user_choice_handler():
    """Provide user with help page navigation options."""
    selection = input('Key option and press Enter: ')
    if selection == '1':
        help_add_ride.show_help_add_ride()
    elif selection == '2':
        help_edit_ride.show_help_edit_ride()
    elif selection == '3':
        help_add_note.show_help_add_note()
    elif selection == '4':
        help_delete_ride.show_help_delete_ride()
    elif selection == '5':
        ride_log.show_ride_log()
    elif selection == '6':
        home.show_home()
        print()
    else:
        print('❗️ Error: Invalid choice. Please try again.')
