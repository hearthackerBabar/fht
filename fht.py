#!/data/data/com.termux/files/usr/bin/bash

# Navbar for Termux Tool

# Print the navbar
print_navbar() {
    echo "==============================="
    echo "         Facebook Tool         "
    echo "==============================="
    echo
}

# Menu
menu() {
    clear
    print_navbar
    echo "1. Extract user's public information"
    echo "2. Download user's profile picture"
    echo "3. Send friend request"
    echo "4. Exit"
    echo
    read -p "Enter your choice: " choice
    case $choice in
        1) extract_info ;;
        2) download_profile_picture ;;
        3) send_friend_request ;;
        4) exit ;;
        *) echo "Invalid choice. Please try again." ; menu ;;
    esac
}

# Get Facebook account link from the user
get_account_link() {
    clear
    print_navbar
    echo "Paste the user's Facebook account link:"
    read -p "Link: " account_link
    echo
    echo "Enter the user's name:"
    read -p "Name: " user_name
    echo
    echo "Enter the user's ID number:"
    read -p "ID Number: " user_id
    echo
    echo "Account link: $account_link"
    echo "Name: $user_name"
    echo "ID Number: $user_id"
    echo
    read -p "Press Enter to continue..." enter_key
    menu
}

# Extract user's public information
extract_info() {
    get_account_link
}

# Download user's profile picture
download_profile_picture() {
    get_account_link
}

# Send friend request
send_friend_request() {
    get_account_link
}

# Main executio
menu
