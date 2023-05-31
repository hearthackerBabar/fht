#!/usr/bin/env python2

# Navbar for Termux Tool

# Print the navbar
def print_navbar():
    print("===============================")
    print("         Facebook Tool         ")
    print("===============================")
    print

# Menu
def menu():
    clear()
    print_navbar()
    print("1. Extract user's public information")
    print("2. Download user's profile picture")
    print("3. Send friend request")
    print("4. Exit")
    print
    choice = raw_input("Enter your choice: ")
    if choice == '1':
        extract_info()
    elif choice == '2':
        download_profile_picture()
    elif choice == '3':
        send_friend_request()
    elif choice == '4':
        exit()
    else:
        print("Invalid choice. Please try again.")
        menu()

# Get Facebook account link from the user
def get_account_link():
    clear()
    print_navbar()
    account_link = raw_input("Paste the user's Facebook account link: ")
    print
    user_name = raw_input("Enter the user's name: ")
    print
    user_id = raw_input("Enter the user's ID number: ")
    print
    print("Account link: " + account_link)
    print("Name: " + user_name)
    print("ID Number: " + user_id)
    print
    raw_input("Press Enter to continue...")
    menu()

# Extract user's public information
def extract_info():
    get_account_link()

# Download user's profile picture
def download_profile_picture():
    get_account_link()

# Send friend request
def send_friend_request():
    get_account_link()

# Main execution
menu()
