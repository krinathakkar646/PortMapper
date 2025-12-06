import sys
import socket
from datetime import datetime

#Tool: PortMapper 
#Description: A custom TCP Port Scanner for network reconnaissance.
#Version: 1.0

#1. DEFINE OUR TARGET
target = "scame.nmap.org"

#2. ADD BANNER
print("-" * 50)
print(f"SCANNING TARGET : {target}")
print(f"TIME STARTED : {str(datetime.now())}")
print("-" * 50)

#3. SCANNING 
try:
	for port in range(1,100):
		# CREATE A SOCKET OBJECT 
		s= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		# CREATE TIMEOUT FOR CLOSED PORT
		socket.setdefaulttimeout(1)
		# ATTEMPT TO CONNECT 
		result = s.connect_ex((target , port))

		if result==0:
			print(f"Port {port} is Open ")
		s.close()

except KeyboardInterrupt:
	print ("\n Exiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()
	
print("-" * 50)
print("[*] Scan Complete.")
