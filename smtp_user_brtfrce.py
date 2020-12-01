 
#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

import socket
import sys
from termcolor import colored
#importing the required libraries

#conditional statement for grabing [sys] arguments for username and ip address
if len(sys.argv) != 3:
	print(colored("usage script.py <username> <target-ip>", "red"))
	sys.exit(0)

#initiating socket to form network connections
s = socket.socket()
connect = s.connect((sys.argv[2], 25))
data = s.recv(1024).decode()

#command variable containing data to send to the server
command = 'VRFY ' + sys.argv[1] + '\n'

#The function containing the final code to interact with the server and also receive the data back from the SMTP server
def brtmgc():
	s.send(command.encode())
	result = s.recv(1024)
	fin_result = result.decode()
	valid = '550'
	if valid.encode() in result:
		print(colored(sys.argv[1] + " is not a valid user..", "red"))
	else:
		print(colored(sys.argv[1] + " is a valid user..", 'blue', attrs=['bold']))
	s.close()

#defining main function containing the brtmgc fucntion
def main():
	brtmgc()

#final main function to run the whole function
main()
