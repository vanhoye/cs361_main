from views import help


def show_help_edit_ride():
    """Prints step by step instructions on how to edit a ride."""
    print('='*40)
    print("|        ➕ HOW TO EDIT A RIDE         |")
    print('='*40)
    print()
    print('-Navigate to the Ride Log Page')
    print('-Select a Ride and View Ride Details')
    print('-From the Ride Details Page, choose the Edit Ride option')
    print()
    print("-The prompts will show each ride element's current value")
    print("-Press Enter to keep it or type a new value to change it")
    print()

    # Return to help menu
    user_choice = input("Press Enter to return to Help Menu: ")
    if user_choice == '':
        help.show_help()
    else:
        print("'❗️ Error: Invalid choice. Please try again.'")
