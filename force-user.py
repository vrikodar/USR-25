 
#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

import os
import sys
#import the required libraries

#list of usernames to test
list = ['john','ftp','Odis','Yagi','Edwardo','Herlihy','Leandro','Norberg','Maximo','Duford', 'admin', 'root', 'bob', 'jugnu', 'manglu']

#defining the IP variable to receiving the IP address of the server
IP = sys.argv[1]

#A for loop to run the main script for each username in the defined list
for user in list:
	os.system(f'python3 smtp_user_brtfrce.py {user} {IP}')
