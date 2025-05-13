# DCR whisper11@protonmail.com
# 2025.05.13
# To do:
#   1. Add a function to clean up color selection.
#

import requests
import os
import threading
import time

API_BASE = "https://api.nomi.ai/v1"
API_KEY = "ENTER YOUR API KEY HERE" # Replace with your actual API key
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# This is a placeholder for the clear up of color codes
# colors = ("\033[0m", "\033[91m", "\033[92m", "\033[94m", "\033[95m", "\033[96m", "\033[93m")

# Class to hold color codes
class bcolors:
    nomie_chat_color = '\033[0m'
    self_chat_color = '\033[0m'
    error_color = '\033[0m'
    menu = '\033[0m'
    end = '\033[0m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow= '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the color options and set the colors
def color_choice():
    clear_screen()
    print("----------------------------------")
    print("Color Options:")
    print(bcolors.end + "0 = Default" + "    " + bcolors.red +"1 = Red")
    print(bcolors.green + "2 = Green" + "      " + bcolors.blue + "3 = Blue")
    print(bcolors.purple + "4 = Purple" + "     " + bcolors.cyan + "5 = Cyan")
    print(bcolors.yellow + "6 = Yellow" + bcolors.end)
    print("----------------------------------\n")
    # Get user input for menu colors
    menu_color = input(bcolors.menu + "Enter the number for the Menu color: ")
    if menu_color == "0":
        bcolors.menu = '\033[0m'
    elif menu_color == "1":
        bcolors.menu = '\033[91m'
    elif menu_color == "2":
        bcolors.menu = '\033[92m'
    elif menu_color == "3":
        bcolors.menu = '\033[94m'
    elif menu_color == "4":
        bcolors.menu = '\033[95m'
    elif menu_color == "5":
        bcolors.menu = '\033[96m'
    elif menu_color == "6":
        bcolors.menu = '\033[93m'
    else:
        print(bcolors.error_color + "Invalid choice, defaulting to no color." + bcolors.menu)
        bcolors.menu = '\033[0m'
    # Get user input for self chat colors  
    self_chat_color = input(bcolors.menu + "Enter the number for the Self chat color: ")
    if self_chat_color == "0":
        bcolors.self_chat_color = '\033[0m'
    elif self_chat_color == "1":
        bcolors.self_chat_color = '\033[91m'
    elif self_chat_color == "2":
        bcolors.self_chat_color = '\033[92m'
    elif self_chat_color == "3":
        bcolors.self_chat_color = '\033[94m'
    elif self_chat_color == "4":
        bcolors.self_chat_color = '\033[95m'
    elif self_chat_color == "5":
        bcolors.self_chat_color = '\033[96m'
    elif self_chat_color == "6":
        bcolors.self_chat_color = '\033[93m'
    else:
        print(bcolors.error_color + "Invalid choice, defaulting to no color." + bcolors.menu)
        bcolors.self_chat_color = '\033[0m'
    # Get user input for nomi chat colors
    nomie_chat_color = input(bcolors.menu + "Enter the number for the Nomi chat color: ")
    if nomie_chat_color == "0":
        bcolors.nomie_chat_color = '\033[0m'
    elif nomie_chat_color == "1":
        bcolors.nomie_chat_color = '\033[91m'
    elif nomie_chat_color == "2":
        bcolors.nomie_chat_color = '\033[92m'
    elif nomie_chat_color == "3":
        bcolors.nomie_chat_color = '\033[94m'
    elif nomie_chat_color == "4":
        bcolors.nomie_chat_color = '\033[95m'
    elif nomie_chat_color == "5":
        bcolors.nomie_chat_color = '\033[96m'
    elif nomie_chat_color == "6":
        bcolors.nomie_chat_color = '\033[93m'
    else:
        print(bcolors.error_color + "Invalid choice, defaulting to no color." + bcolors.menu)
        bcolors.nomie_chat_color = '\033[0m'
    # Get user input for error colors    
    error_color = input(bcolors.menu + "Enter the number for the Error messages color: ")
    if error_color == "0":
        bcolors.error_color = '\033[0m'
    elif error_color == "1":
        bcolors.error_color = '\033[91m'
    elif error_color == "2":
        bcolors.error_color = '\033[92m'
    elif error_color == "3":
        bcolors.error_color = '\033[94m'
    elif error_color == "4":
        bcolors.error_color = '\033[95m'
    elif error_color == "5":
        bcolors.error_color = '\033[96m'
    elif error_color == "6":
        bcolors.error_color = '\033[93m'
    else:
        print(bcolors.error_color + "Invalid choice, defaulting to no color." + bcolors.menu)
    
    clear_screen()
    print(bcolors.menu + "----------------------------------")
    print("Color Options Set!")
    print("----------------------------------\n")
    print(bcolors.nomie_chat_color + "Nomi Chat Color")
    print(bcolors.menu + "Menu Color")
    print(bcolors.self_chat_color + "Self Chat Color")
    print(bcolors.error_color + "Error Color")
    print(bcolors.menu + "----------------------------------\n")
    print("Press Enter to return to the main menu.")
    input()

# Function to test connection to Nomi.ai        
def connect_to_nomi():
    try:
        clear_screen()
        response = requests.get(f"{API_BASE}/nomis", headers=HEADERS)
        if response.status_code == 200:
            print(bcolors.menu + "----------------------------------")
            print("Successfully connected to Nomi.ai!")
            print("----------------------------------")
        else:
            bcolors.error_color 
            print(f"Failed to connect. Status code: {response.status_code}")
            bcolors.end
    except Exception as e:
        bcolors.error_color 
        print(f"An error occurred: {e}")
        bcolors.end
        
# Function to list available Nomis        
def list_nomies():
    clear_screen()
    response = requests.get(f"{API_BASE}/nomis", headers=HEADERS)
    if response.status_code == 200:
        nomies = response.json().get("nomis", [])
        print(bcolors.menu + "----------------------------------")
        print("Available Nomis")
        print("----------------------------------\n")
        for idx, nomi in enumerate(nomies, 1):
            print(f"{nomi['name']} (ID: {nomi['uuid']})")
        return nomies
    else:
        print(bcolors.error_color + "Failed to fetch nomies:" + bcolors.menu, response.text)
        return []

# Function to select a Nomi to chat with
def select_nomies():
    clear_screen()
    response = requests.get(f"{API_BASE}/nomis", headers=HEADERS)
    if response.status_code == 200:
        nomies = response.json().get("nomis", [])
        print(bcolors.menu + "----------------------------------")
        print("Choose a Nomi")
        print("----------------------------------\n")
        for idx, nomi in enumerate(nomies, 1):
            print(f"{idx}. {nomi['name']}")
        return nomies
    else:
        print(bcolors.error_color + "Failed to fetch nomies:" + bcolors.menu, response.text)
        return []

# Function to chat with a selected Nomi
def chat_with_nomi(nomi_id, nomie_name):
    clear_screen()
    print(bcolors.menu + "----------------------------------" + bcolors.nomie_chat_color)
    print(f"Chatting with {nomie_name} (ID: {nomi_id}")
    print(bcolors.menu + "Type 'exit' to end chat.")
    print("----------------------------------\n")
    while True:
        user_input = input(bcolors.self_chat_color +"You: ")
        if user_input.lower() == "exit" or user_input.lower() == "":
            break
        payload = {"messageText": user_input, "uuid": nomi_id}

        # Blinking star setup
        stop_blink = False
        def blink_star():
            while not stop_blink:
                print(bcolors.menu + "\rWaiting for reply * ", end="", flush=True)
                time.sleep(0.5)
                print(bcolors.menu + "\rWaiting for reply   ", end="", flush=True)
                time.sleep(0.5)

        blink_thread = threading.Thread(target=blink_star)
        blink_thread.start()

        response = requests.post(f"{API_BASE}/nomis/{nomi_id}/chat", headers=HEADERS, json=payload)

        stop_blink = True
        blink_thread.join()
        print("\r" + " " * 30 + "\r", end="")  # Clear the blinking line

        if response.status_code == 200:
            reply = response.json().get("replyMessage", {}).get("text", "")
            print(f"{bcolors.nomie_chat_color}{nomie_name}: {reply}{bcolors.end}")
        else:
            print(bcolors.error_color + "Error chatting with Nomi:" + bcolors.menu, response.text)

# Main function to run the program
def main():
    clear_screen()
    while True:
        print(bcolors.menu + "\nMain Menu:")
        print("1. List Nomis")
        print("2. Select a Nomi to chat with")
        print("3. Color Options")
        print("4. Test Connection")
        print("5. Exit")
        choice = input("Enter your choice: " + bcolors.end)
        if choice == "1":
            list_nomies()
        elif choice == "2":
            nomies = select_nomies()
            if not nomies:
                continue
            idx = input("Enter the number of the Nomi to chat with: ")
            try:
                idx = int(idx) - 1
                if 0 <= idx < len(nomies):
                    chat_with_nomi(nomies[idx]['uuid'], nomie_name=nomies[idx]['name'])
                else:
                    print(bcolors.error_color + "Invalid selection." + bcolors.menu)
            except ValueError:
                print(bcolors.error_color + "Invalid input." + bcolors.menu)
        elif choice == "3":
            color_choice()
        elif choice == "4":
            connect_to_nomi()        
        elif choice == "5" or choice == "":
            break
        else:
            print(bcolors.error_color + "Invalid choice." + bcolors.menu)
            
if __name__ == "__main__":
    main()