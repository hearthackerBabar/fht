import os
import webbrowser
import requests
from bs4 import BeautifulSoup

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
    
    # Extract username from Facebook profile
    username = get_username(account_link)
    print("Profile Username: " + username)
    raw_input("Press Enter to continue...")
    main_menu()

# Extract username from Facebook profile
def get_username(account_link):
    # Open the Facebook profile in a web browser
    webbrowser.open_new_tab(account_link)
    
    # Make a GET request to the Facebook profile page
    response = requests.get(account_link)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the element containing the profile username
    username_element = soup.find('a', class_='_2nlw _2nlv')
    
    # Extract the username
    username = username_element.text.strip()
    
    return username

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
