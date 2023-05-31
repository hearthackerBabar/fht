import os
import re

# Clear the screen
def clear_screen():
    os.system('clear')

# Function to display the navbar
def print_navbar():
    print("===============================")
    print("      Welcome To FHT Tool      ")
    print("===============================")
    print()

# Main menu
def main_menu():
    clear_screen()
    print_navbar()
    print("1. FB Cracking")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
    print()
    choice = raw_input("Enter your choice: ")
    if choice == '1':
        option_1()
    elif choice == '2':
        option_2()
    elif choice == '3':
        option_3()
    elif choice == '4':
        exit()
    else:
        print("Invalid choice. Please try again.")
        raw_input("Press Enter to continue...")
        main_menu()

# Example option 1
def option_1():
    clear_screen()
    print_navbar()
    print("You Have Selected Option No.1 FB Cracking")
    raw_input("Press Enter to continue...")
    clear_screen()
    print_navbar()
    print("Please paste the Facebook account link:")
    account_link = raw_input("Link: ")
    
    # Extract user's first name and last name from profile link
    first_name, last_name = get_name_from_profile_link(account_link)
    
    if first_name and last_name:
        print("Welcome, " + first_name + " " + last_name)
    else:
        print("Failed to retrieve name from profile link.")
    
    raw_input("Press Enter to continue...")
    main_menu()

# Extract user's first name and last name from profile link
def get_name_from_profile_link(profile_link):
    # Extract the user ID from the profile link
    user_id = re.search(r"(?<=facebook\.com\/)(\d+)", profile_link)
    
    if user_id:
        # Retrieve the user's first name and last name
        # Replace this code with your own logic to fetch user data from the Facebook API or other means
        first_name = "John"
        last_name = "Doe"
        
        return first_name, last_name
    
    return None, None

# Example option 2
def option_2():
    clear_screen()
    print_navbar()
    print("This is Option 2.")
    print()
    raw_input("Press Enter to continue...")
    main_menu()

# Example option 3
def option_3():
    clear_screen()
    print_navbar()
    print("This is Option 3.")
    print()
    raw_input("Press Enter to continue...")

# Main execution
main_menu()
