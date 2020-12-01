#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

import os

list = ['john','ftp','Odis','Yagi','Edwardo','Herlihy','Leandro','Norberg','Maximo','Duford', 'admin', 'root', 'bob', 'jugnu', 'manglu']
#List of users to check for the smtp service...


#a loop to run the final script for each user present in the list
for user in list:
	os.system(f'python3 smtp_user_brtfrce.py {user}')
