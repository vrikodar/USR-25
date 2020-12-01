import os

list = ['john','ftp','Odis','Yagi','Edwardo','Herlihy','Leandro','Norberg','Maximo','Duford', 'admin', 'root', 'bob', 'jugnu', 'manglu']

for user in list:
	os.system(f'python3 smtp_user_brtfrce.py {user}')
