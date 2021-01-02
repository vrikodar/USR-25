#By SxNade
#https://github.com/SxNade/SMTP-USER-BRTFRCE
#CONTRIBUTE

import socket
import sys
from termcolor import colored
import os
#importing the required libraries

target_ip = sys.argv[1]
user_file = sys.argv[2]

#conditional statement for grabing [sys] arguments for username and ip address
if len(sys.argv) != 3:
	print(colored("usage script.py <username> <target-ip>", "red"))
	sys.exit(0)


if os.path.exists(user_file) == False:
	print(colored('[!]File Not Found....exiting now..!', 'red', attrs=['bold']))
	sys.exit(0)

with open(f'{user_file}', 'r') as file:
	for line in file.readlines():
		user = line.strip()
		#command variable containing data to send to the server
		command = 'VRFY ' + user + '\n'
		try:
			s = socket.socket()
			connect = s.connect((target_ip, 25))
			data = s.recv(1024).decode()
			s.send(command.encode())
			result = s.recv(1024)
			fin_result = result.decode()
			valid = '550'
			if valid.encode() in result:
				print(colored(f"\n[!]{user} is not a valid user..", "red", attrs=['bold']))
			else:
				print(colored(f"\n\n[+] {user} is a valid user..\n\n", 'green', attrs=['bold']))
			s.close()
		except KeyboardInterrupt:
			ask = input("\n\nDo you want to stop Bruteforce: ")
			if ask == "Y":
				sys.exit(0)
			elif ask == "N":
				pass
			else:
				print(colored("\nUnexpected input"))
				sys.exit(0)



