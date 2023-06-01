import os
import requests
import re
import json

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
    choice = input("Enter your choice: ")  # Update raw_input to input for Python 3 compatibility
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
        input("Press Enter to continue...")
    main_menu()

# Example option 1
def option_1():
    clear_screen()
    print_navbar()
    print("You Have Selected Option No.1 FB Cracking")
    input("Press Enter to continue...")
    clear_screen()
    print_navbar()
    access_token = input("Enter your Facebook access token: ")
    
    # Login using the access token
    account_name = login_with_token(access_token)
    
    if account_name:
        print("Welcome, {}!".format(account_name))
        print()
        print("Please paste the Facebook account link:")
        account_link = input("Link: ")
        
        # Extract Facebook profile name from profile link
        first_name, last_name = get_profile_name(account_link)
        
        if first_name and last_name:
            profile_name = "{} {}".format(first_name, last_name)
            print("Profile Name: {}".format(profile_name))
        else:
            print("Failed to retrieve profile name.")
    else:
        print("Login failed. Please check your access token.")
    
    input("Press Enter to continue...")
    main_menu()

# Login using the access token
def login_with_token(access_token):
    # Make a GET request to the Facebook Graph API
    api_url = "https://graph.facebook.com/v13.0/me?fields=name&access_token=" + access_token
    response = requests.get(api_url)
    
    # Parse the JSON response
    data = response.json()
    
    # Check if login was successful
    if response.status_code == 200 and "name" in data:
        return data["name"]
    else:
        return None

# Retrieve Facebook profile name from profile link
def get_profile_name(profile_link):
    # Extract the user ID from the profile link
    user_id = re.search(r"(?<=facebook\.com\/)(\d+)", profile_link)
    
    if user_id:
        # Make a GET request to the Facebook API
        api_url = "https://graph.facebook.com/{user_id.group(1)}"
        response = requests.get(api_url)
        
        # Parse the JSON response
        data = response.json()
        
        # Check if profile exists and retrieve the name
        if response.status_code == 200 and "name" in data:
            name_parts = data["name"].split()
            if len(name_parts) >= 2:
                return name_parts[0], name_parts[-1]
    
    return None, None
main_menu()

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
main_menu()

# Main execution
main_menu()
