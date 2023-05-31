#!/usr/bin/env python2

import os

# Clear the screen
def clear_screen():
    os.system('clear')

# Function to display the navbar
def print_navbar():
    print("===============================")
    print("        Termux Tool (Python 2) ")
    print("===============================")
    print()

# Main menu
def main_menu():
    clear_screen()
    print_navbar()
    print("1. Option 1")
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
    print("This is Option 1.")
    print()
    raw_input("Press Enter to continue...")
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
