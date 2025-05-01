from views import help


def show_help_add_note():
    """Prints step by step instructions on how to add a note to a ride."""
    print('='*40)
    print("|        ➕ HOW TO ADD A NOTE          |")
    print('='*40)
    print()
    print('-Navigate to the Ride Log Page')
    print('-Select a ride and View Ride Details')
    print('-From the Ride Details Page, choose the Add Note option')
    print('Add your note, pressing Enter to save')

    # Return to help menu
    user_choice = input("Press Enter to return to Help Menu: ")
    if user_choice == '':
        help.show_help()
    else:
        print("'❗️ Error: Invalid choice. Please try again.'")
