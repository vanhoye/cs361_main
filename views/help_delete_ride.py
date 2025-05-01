from views import help


def show_help_delete_ride():
    """Prints step by step instructions on how to delete a ride."""
    print('='*40)
    print("|       ➕ HOW TO DELETE A RIDE        |")
    print('='*40)
    print()

    print('-Navigate to the Ride Log Page')
    print('-Select a ride and View Ride Details')
    print('-From the Ride Details Page, choose the Delete Ride Option')
    print('-Confirm or cancel the deletion by typing yes or no')
    print('❗️PLEASE NOTE: THIS ACTION CANNOT BE UNDONE❗️')
    print()

    # Return to help page
    user_choice = input("Press Enter to return to Help Menu: ")
    if user_choice == '':
        help.show_help()
    else:
        print("'❗️ Error: Invalid choice. Please try again.'")
