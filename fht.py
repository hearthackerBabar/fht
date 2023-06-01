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
    print("      Owner : Babar Ali        ")
    print("      Phone No. 03000448415    ")
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
    access_token = raw_input("Enter your Facebook access token: ")
    
    # Login using the access token
    account_name = login_with_token(access_token)
    
    if account_name:
        print("Welcome, " + account_name)
        print()
        print("Please paste the Facebook account link:")
        account_link = raw_input("Link: ")
        
        # Extract Facebook profile name from profile link
        profile_name = get_profile_name(account_link)
        
        if profile_name:
            print("Profile Name: " + profile_name)
        else:
            print("Failed to retrieve profile name.")
    else:
        print("Login failed. Please check your access token.")
    
    raw_input("Press Enter to continue...")
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
        # Make a GET request to the Facebook Graph API
        api_url = "https://graph.facebook.com/{user_id.group(1)}"
        response = requests.get(api_url)

        # Parse the JSON response
        data = response.json()

        # Check if profile exists and retrieve the name
        if response.status_code == 200 and "first_name" in data and "last_name" in data:
            return data["first_name"], data["last_name"]
    
    return None, None


# Example option 2
def option_2():
    clear_screen()
    print_navbar()
    print("You Have Selected Option No.2")
    raw_input("Press Enter to continue...")
    clear_screen()
    print_navbar()
    # Add your code for option 2 here
    
    raw_input("Press Enter to continue...")
    main_menu()

# Example option 3
def option_3():
    clear_screen()
    print_navbar()a
    print("You Have Selected Option No.3")
    raw_input("Press Enter to continue...")
    clear_screen()
    print_navbar()
    # Add your code for option 3 here
    
    raw_input("Press Enter to continue...")
    main_menu()

# Main entry point
if __name__ == "__main__":
    main_menu()
