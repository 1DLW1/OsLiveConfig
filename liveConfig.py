import subprocess, time, os, colorama
from colorama import Fore

#clean screen
def limpieza():
    os.system('clear')

limpieza()
print(Fore.LIGHTWHITE_EX + '[' + Fore.LIGHTBLUE_EX + 'Live Os Configuration' + Fore.LIGHTWHITE_EX + ']\n')

#Sync timer zone
def timezone():
    #set timezone as you want
    timezone='Europe/Dublin'
    subprocess.run('sudo timedatectl set-timezone ' + timezone + ' && timedatectl', shell=True)
    #turn on ntp sync
    subprocess.run('sudo timedatectl set-ntp on', shell=True)


#Folder of the network adapter driver
carpeta='rtl8812au-5.6.4.2'
ruta_carpeta = os.path.join(os.getcwd(), carpeta)

#Installation of network adapter driver
if os.path.exists(ruta_carpeta):
    os.chdir(carpeta)
    subprocess.run('sudo dkms_install && sudo make && sudo make install',shell=True)
    #Assignment of the essid of the interface
    subprocess.run('sudo iwconfig wlan0 essid off && sudo iwconfig wlan0 essid TpLink && sudo ifconfig wlan0 up',shell=True)
    subprocess.run('sudo apt update && sudo apt upgrade',shell=True)

else:
    print(f"La carpeta '{carpeta}' no está en el directorio actual.")
    