import subprocess
import os
import colorama
from colorama import Fore

# Function to clear the screen
def clear_screen():
    os.system('clear')

# Function to set the time zone
def set_timezone():
    # Set the desired time zone
    timezone = 'Europe/Dublin'
    subprocess.run(f'sudo timedatectl set-timezone {timezone} && timedatectl', shell=True)
    # Enable NTP synchronization
    subprocess.run('sudo timedatectl set-ntp on', shell=True)

# Function to install the network adapter driver
def install_driver(folder_path, folder_name):
    if os.path.exists(folder_path):
        os.chdir(folder_name)
        subprocess.run('sudo make dkms_install && sudo make && sudo make install', shell=True)
        # Assign the ESSID of the interface
        subprocess.run('sudo iwconfig wlan0 essid off && sudo iwconfig wlan0 essid TpLink && sudo ifconfig wlan0 up', shell=True)
        print('\n')
        set_timezone()
        print('\n')
        subprocess.run('sudo apt update && sudo apt upgrade', shell=True)
    else:
        print(f"The folder '{folder_name}' does not exist in the current directory.")

def main():
    # Clear the screen
    clear_screen()
    print(Fore.LIGHTWHITE_EX + '[' + Fore.LIGHTBLUE_EX + 'Live Os Configuration' + Fore.LIGHTWHITE_EX + ']\n')
    
    # Folder of the network adapter driver
    folder_name = 'rtl8812au-5.6.4.2'
    folder_path = os.path.join(os.getcwd(), folder_name)

    # Install the network adapter driver
    install_driver(folder_path, folder_name)

if __name__ == "__main__":
    main()