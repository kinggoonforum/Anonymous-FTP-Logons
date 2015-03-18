#=======================================================#
# Name:	Anon_FTP_Logon.py v1.0			 	#
# By:	Mad City Hacker				 	#
# Date:	3/12/2015				 	#
# Blog: madcityhacker.com			 	#
# Syntax: python Anon_FTP_Logon.py <CIDR Network>	#
#=======================================================#

import sys
from multiprocessing import Pool, freeze_support
from ftplib import FTP
from netaddr import *

ip = IPNetwork(sys.argv[1])

def anonLogin(hostname):
	try:
		# Attempt anonymous FTP connection to host
		ftp = FTP(str(hostname))
		ftp.login('anonymous','anonymous@badpractice.com')
		print '\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.'
		ftp.quit()
		return

	except Exception, e:
		return
        

# Multiprocessing to reduce time needed to scan a network. Change the "processes=" value
# (Default 10) to specify how many processes to run at once

if __name__ == '__main__':
	freeze_support()
	pool = Pool(processes=10)
	pages = pool.map(anonLogin, ip)