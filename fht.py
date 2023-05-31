import os
import requests

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
    access_token = raw_input("Enter your Facebook access token: ")
    
    # Get user information using access token
    user_info = get_user_info(access_token)
    if user_info:
        account_name = "Welcome, " + user_info.get("first_name") + " " + user_info.get("last_name")
        print(account_name)
    else:
        print("Failed to retrieve account information.")
    
    raw_input("Press Enter to continue...")
    clear_screen()
    print_navbar()
    print("Please paste the Facebook account link:")
    account_link = raw_input("Link: ")
    
    # Extract Facebook account name from profile link
    account_name = get_account_name(account_link, access_token)
    if account_name:
        print("Account Name: " + account_name)
    else:
        print("Failed to retrieve account name.")
    
    raw_input("Press Enter to continue...")
    main_menu()

# Retrieve user information using access token
def get_user_info(access_token):
    # Make a GET request to the Facebook Graph API
    api_url = "https://graph.facebook.com/me?fields=first_name,last_name&access_token=" + access_token
    response = requests.get(api_url)

    # Parse the JSON response
    data = response.json()

    return data

# Retrieve Facebook account name from profile link using Facebook Graph API
def get_account_name(profile_link, access_token):
    # Extract the user ID from the profile link
    user_id = profile_link.split("/")[-1]

    # Make a GET request to the Facebook Graph API
    api_url = "https://graph.facebook.com/" + user_id + "?fields=name&access_token=" + access_token
    response = requests.get(api_url)

    # Parse the JSON response
    data = response.json()

    # Extract the account name
    account_name = data.get("name")

    return account_name

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
    main_menu
