#By SxNade
#https://github.com/SxNade/SMTP-USER-BRTFRCE
#CONTRIBUTE

import socket
import sys
from termcolor import colored
import os
import time
#importing the required libraries

golo = '''
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`  
'''


#conditional statement for grabing [sys] arguments for username and ip address

print(golo)
time.sleep(1)
print("\n (v2.0) starting...")

#check for correct number of arguments
if len(sys.argv) != 3:
	print(colored("\nusage script.py <target-ip> <username-file--or--path> \n", 'white', attrs=['reverse', 'blink']))
	sys.exit(0)

target_ip = sys.argv[1]
user_file = sys.argv[2]
#grabbing the necessary arguments

#check if the given file exists on the system
if os.path.exists(user_file) == False:
	print(colored('[!]File Not Found....exiting now..!', 'red', attrs=['bold']))
	sys.exit(0)

#reading passwords from the file!
with open(f'{user_file}', 'r') as file:
	for line in file.readlines():
		user = line.strip()
		#command variable containing data to send to the server
		command = 'VRFY ' + user + '\n'
		#using socket to connect to SMTP on the Target
		try:
			s = socket.socket()
			connect = s.connect((target_ip, 25))
			data = s.recv(1024).decode()
			s.send(command.encode())
			result = s.recv(1024)
			fin_result = result.decode()
			valid = 'exists'
			if valid.encode() in result:
				print(colored(f"\n\n[+] {user} is a valid user..\n\n", 'green', attrs=['bold']))
			else:
				print(colored(f"\n[!]{user} is not a valid user..", "red", attrs=['bold']))
			s.close()
		except KeyboardInterrupt:
			ask = input("\n\nDo you want to stop Bruteforce(Y/N): ")
			if ask == "Y":
				sys.exit(0)
			elif ask == "N":
				pass
			else:
				print(colored("\nUnexpected input"))
				sys.exit(0)


#BYE
