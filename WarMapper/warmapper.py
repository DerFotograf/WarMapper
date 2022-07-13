import socket
import colorama
from colorama import Fore
import os
from os import system, name
import time
colorama.init()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

os.system("cls")
time.sleep(1)
print(f'''{Fore.YELLOW}
    .....                           s                                                               
 .H8888888x.  '`+                  :8                                                        oec :  
:888888888888x.  !        u.      .88           u.                  .u    .                 @88888  
8~    `"*88888888"  ...ue888b    :888ooo  ...ue888b       uL      .d88B :@8c        u       8"*88%  
!      .  `f""""    888R Y888r -*8888888  888R Y888r  .ue888Nc.. ="8888f8888r    us888u.    8b.     
 ~:...-` :8L <)88:  888R I888>   8888     888R I888> d88E`"888E`   4888>'88"  .@88 "8888"  u888888> 
    .   :888:>X88!  888R I888>   8888     888R I888> 888E  888E    4888> '    9888  9888    8888R   
 :~"88x 48888X ^`   888R I888>   8888     888R I888> 888E  888E    4888>      9888  9888    8888P   
<  :888k'88888X    u8888cJ888   .8888Lu= u8888cJ888  888E  888E   .d888L .+   9888  9888    *888>   
  d8888f '88888X    "*888*P"    ^%888*    "*888*P"   888& .888E   ^"8888*"    9888  9888    4888    
 :8888!    ?8888>     'Y"         'Y"       'Y"      *888" 888&      "Y"      "888*""888"   '888    
 X888!      8888~                                     `"   "888E               ^Y"   ^Y'     88R    
 '888       X88f                                     .dWi   `88E                             88>    
  '%8:     .8*"                                      4888~  J8%                              48     
     ^----~"`                                         ^"===*"`                               '8     

''')

time.sleep(2)

ipadrr = input(f"{Fore.RED}>> {Fore.BLUE}Introduce la IP a escanear: ")
port = int(input(f"{Fore.RED}>> {Fore.BLUE}Introduce el puerto que quieras escanear: "))

def warMapper(port):
    if s.connect_ex((ipadrr, port)):
        print(f"{Fore.RED}- El puerto", port, f"{Fore.RED}está cerrado...")
    else:
        print(f"{Fore.GREEN}- El puerto", port, f"{Fore.GREEN}está abierto.")

warMapper(port)