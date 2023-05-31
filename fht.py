import os
import requests
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

    # Retrieve profile first name and last name
    profile_name = get_profile_name(account_link)

    if profile_name:
        print("Profile Name: " + profile_name)
    else:
        print("Failed to retrieve profile name.")

    raw_input("Press Enter to continue...")
    main_menu()

# Retrieve profile first name and last name from Facebook profile
def get_profile_name(profile_link):
    # Extract the user ID from the profile link
    user_id_match = re.search(r"(?<=facebook\.com\/)(\d+)", profile_link)

    if user_id_match:
        user_id = user_id_match.group(1)

        # Make a GET request to the Facebook Graph API
        api_url = "https://graph.facebook.com/{}".format(user_id)
        response = requests.get(api_url)

        # Parse the JSON response
        data = response.json()

        # Check if profile exists and retrieve the name
        if response.status_code == 200 and "first_name" in data and "last_name" in data:
            first_name = data["first_name"]
            last_name = data["last_name"]
            return "{} {}".format(first_name, last_name)

    return None

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
