# Foxy Code Pixel
# Github   : https://github.com/FoxyCodePixel 
# Telegram : https://telegram.me/IvanLipovsky


# LIbraries
import os
import sys
import time
from colorama import Fore as c


# clear Terminal (optional)
# os.system("clear")

# Icon
icon = ( c.BLUE + """
""" + c.BLUE + """         .__  _____.__ """ + c.RED + """ ________    
""" + c.BLUE + """ __  _  _|__|/ ____\__|""" + c.RED + """ \______ \   
""" + c.BLUE + """ \ \/ \/ /  \   __\|  |""" + c.RED + """  |    |  \  
""" + c.BLUE + """  \     /|  ||  |  |  |""" + c.RED + """  |    `   \ 
""" + c.BLUE + """   \/\_/ |__||__|  |__|""" + c.RED + """ /_______  / 
""" + c.GREEN + """   Simple Wifi Manager""" + c.RED + """         \/ 
""" + c.GREEN + """   By FoxyCodePixel
""" + c.RESET)

# Menu
menu = ( """
 """ + c.RED + """[1] """ + c.GREEN + """Show interfaces
 """ + c.RED + """[2] """ + c.GREEN + """Turn wifi on
 """ + c.RED + """[3] """ + c.GREEN + """Turn wifi off
 """ + c.RED + """[4] """ + c.GREEN + """Show wifi devices 
 """ + c.RED + """[5] """ + c.GREEN + """Connect to wifi 
 """ + c.RED + """[0] """ + c.GREEN + """Exit """ + c.RESET )

print(icon)
print(menu)

# Main Function
def main():

  # input option
  option = input( c.CYAN + "\nChoose your option : " + c.RED)

  if option == "1":
    os.system("nmcli d")
    main()

  if option == "2":
    os.system("nmcli r wifi on")
    main()

  if option == "3":
    os.system("nmcli r wifi off")
    main()

  if option == "4":
    os.system("nmcli d wifi list")
    main()

  if option == "5":
    ssid   = input(c.YELLOW + "\n [*] Enter the wifi name : " + c.RED)
    passwd = input(c.YELLOW + "\n [*] Enter the password  : " + c.RED)
    print( c.RESET + "\n")
    os.system ("nmcli d wifi connect " + ssid + " password " + passwd)
    main()

  if option == "0":
    sys.exit()

main()
