import socket 
import os

class colours:
	Red = "\033[91m"
	Green = "\033[92m"

	
def ping(host,port,textfile):
	s = socket.socket()
	s.settimeout(1)
	connect = s.connect_ex((host,int(port)))
	if connect == 0:
		try:
			t= socket.gethostbyaddr(host)
			hostname = t[0]
			print (colours.Green + hostname + " "+ "port " + port+ " is open" + " ("+host+") \n")
			textfile.write(hostname + " "+ "port " + port+ " is open" + "( "+ host+ ") \n")
		except:
				print (host + " " + "port "  + port + " is open but no hostname was returned \n")
	else : 
		print (colours.Red + host + " "+ "port " + port+ " is closed \n" )
		textfile.write(host + " "+ " is closed \n")

		
def select ():        ### Selects the network action the user would like to perform ###
	print("1 - Network ping (Pretty useless in this version)")
	print("2 - Socket scan")
	print("3 - Host scan")
	type = input("Please select 1,2 or 3: ")
	if int(type) == 1:
		os.system("cls")
		network_ping()
	if int(type) == 2:
		os.system("cls")
		socket_scan()
	if int(type) == 3:
		os.system("cls")
		host_scan()
	else:
		print ("You must enter one of the options.")
	
	
def network_ping():
	starting_host = input("Input starting host: ")
	final_host = input("Input final host: ")
	sh_split = starting_host.split(".") ### Splits the host IP into individual bytes###
	fh_split = final_host.split(".")
	print("###Scanning###")
	textfile = open("ping"+ " " + starting_host + "-" + final_host + ".txt", "w+")
	if sh_split[0] != fh_split[0]:
		for num in range(int(sh_split[0]),(int(fh_split[0])+1)): 
			oct0 = str(num)
			if num == int(sh_split[0]):
				for num in range(int(sh_split[1]),256):
					oct1 = (oct0 + "." + str(num))
					if num == int(sh_split[1]):
						for num in range(int(sh_split[2]),256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
					elif num == int(fh_split[1]):
						for num in range(0,int(fh_split[1])+1):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
					else :
						for num in range(0,256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")	
			elif num == int(fh_split[0]):
				for num in range(0,int(fh_split[0])+1):
					oct1 = (oct0 + "." + str(num))
					if num == int(sh_split[1]):
						for num in range(int(sh_split[2]),256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
					elif num == int(fh_split[1]):
						for num in range(0,int(fh_split[1])+1):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
					else :
						for num in range(0,256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")	
			else:
				for num in range(0,256):
					oct1 = (oct0 + "." + str(num))
					if num == int(sh_split[1]):
						for num in range(int(sh_split[2]),256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
					elif num == int(fh_split[1]):
						for num in range(0,int(fh_split[1])+1):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
					else :
						for num in range(0,256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
									p.wait()
									if p.poll() == 0:
										print (host + " "+ "is up")
										textfile.write(host + " "+ "is up \n")
									else :
										print (host + " "+ "is down")
										textfile.write(host + " "+ "is down \n")	
	if sh_split[0] == fh_split[0]:
		oct0 = sh_split[0]
		if sh_split[1] != fh_split[1]:
			for num in range(int(sh_split[1]),(int(fh_split[1])+1)): 
				oct1 = (oct0+ "." + str(num))
				if num == int(sh_split[1]):
					for num in range(int(sh_split[2]),256):
						oct2 = (oct1 + "." + str(num))
						if num == int(sh_split[2]):
							for num in range(int(sh_split[3]),256):
								host = (oct2 + "." + str(num))
								p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
								p.wait()
								if p.poll() == 0:
									print (host + " "+ "is up")
									textfile.write(host + " "+ "is up \n")
								else :
									print (host + " "+ "is down")
									textfile.write(host + " "+ "is down \n")
						elif num == int(fh_split[2]):
							for num in range (0,int(fh_split[3])+1):
								host = (oct2 + "." + str(num))
								p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
								p.wait()
								if p.poll() == 0:
									print (host + " "+ "is up")
									textfile.write(host + " "+ "is up \n")
								else :
									print (host + " "+ "is down")
									textfile.write(host + " "+ "is down \n")
						else:
							for num in range (0,256):
								host = (oct2 + "." + str(num))
								p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
								p.wait()
								if p.poll() == 0:
									print (host + " "+ "is up")
									textfile.write(host + " "+ "is up \n")
								else :
									print (host + " "+ "is down")
									textfile.write(host + " "+ "is down \n")
				elif num == int(fh_split[1]):
					for num in range(int(sh_split[2]),256):
						oct2 = (oct1 + "." + str(num))
						if num == int(sh_split[2]):
							for num in range(int(sh_split[3]),256):
								host = (oct2 + "." + str(num))
								p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
								p.wait()
								if p.poll() == 0:
									print (host + " "+ "is up")
									textfile.write(host + " "+ "is up \n")
								else :
									print (host + " "+ "is down")
									textfile.write(host + " "+ "is down \n")
						elif num == int(fh_split[2]):
							for num in range (0,int(fh_split[3])+1):
								host = (oct2 + "." + str(num))
								p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
								p.wait()
								if p.poll() == 0:
									print (host + " "+ "is up")
									textfile.write(host + " "+ "is up \n")
								else :
									print (host + " "+ "is down")
									textfile.write(host + " "+ "is down \n")
						else:
							for num in range (0,256):
								host = (oct2 + "." + str(num))
								p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
								p.wait()
								if p.poll() == 0:
									print (host + " "+ "is up")
									textfile.write(host + " "+ "is up \n")
								else :
									print (host + " "+ "is down")
									textfile.write(host + " "+ "is down \n")
				else :
					for num in range(0,256):
						oct2 = (oct1 + "." + str(num))
						if num == int(sh_split[2]):
							for num in range(int(sh_split[3]),256):
								host = (oct2 + "." + str(num))
								p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
								p.wait()
								if p.poll() == 0:
									print (host + " "+ "is up")
									textfile.write(host + " "+ "is up \n")
								else :
									print (host + " "+ "is down")
									textfile.write(host + " "+ "is down \n")
						elif num == int(fh_split[2]):
							for num in range (0,int(fh_split[3])+1):
								host = (oct2 + "." + str(num))
								p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
								p.wait()
								if p.poll() == 0:
									print (host + " "+ "is up")
									textfile.write(host + " "+ "is up \n")
								else :
									print (host + " "+ "is down")
									textfile.write(host + " "+ "is down \n")
						else:
							for num in range (0,256):
								host = (oct2 + "." + str(num))
								p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
								p.wait()
								if p.poll() == 0:
									print (host + " "+ "is up")
									textfile.write(host + " "+ "is up \n")
								else :
									print (host + " "+ "is down")
									textfile.write(host + " "+ "is down \n")	
		if sh_split[1] == fh_split[1]:
			oct1 = (oct0+ "." + sh_split[1])
			if sh_split[2] != fh_split[2]:
				for num in range(int(sh_split[2]),(int(fh_split[2])+1)): 
					oct2 = (oct1 +"."+str(num))
					if num == int(sh_split[2]):
						for num in range(int(sh_split[3]),256):
							host = (oct2 + "." + str(num))
							p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
							p.wait()
							if p.poll() == 0:
								print (host + " "+ "is up")
								textfile.write(host + " "+ "is up \n")
							else :
								print (host + " "+ "is down")
								textfile.write(host + " "+ "is down \n")
					elif num == int(fh_split[2]):
							for num in range (0,int(fh_split[3])+1):
								host = (oct2 + "." + str(num))
								p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
								p.wait()
								if p.poll() == 0:
									print (host + " "+ "is up")
									textfile.write(host + " "+ "is up \n")
								else :
									print (host + " "+ "is down")
									textfile.write(host + " "+ "is down \n")
					else:
							for num in range (0,256):
								host = (oct2 + "." + str(num))
								p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
								p.wait()
								if p.poll() == 0:
									print (host + " "+ "is up")
									textfile.write(host + " "+ "is up \n")
								else :
									print (host + " "+ "is down")
									textfile.write(host + " "+ "is down \n")
			if sh_split[2] == fh_split[2]:
				oct2 = (oct1+ "." + sh_split[2])
				if sh_split[3] != fh_split[3]:
					for num in range (int(sh_split[3]),int(fh_split[3])+1):
						host = (oct2 + "." + str(num))
						p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
						p.wait()
						if p.poll() == 0:
							print (host + " "+ "is up")
							textfile.write(host + " "+ "is up \n")
						else :
							print (host + " "+ "is down")
							textfile.write(host + " "+ "is down \n")
				if sh_split[3] == fh_split[3]:
					host = (oct2 + "." + sh_split[3])
					p = subprocess.Popen("ping -a -n 2 -l 8 -w 2000 " + host, stdout=textfile)
					p.wait()
					if p.poll() == 0:
						print (host + " "+ "is up")
						textfile.write(host + " "+ "is up \n")
					else :
						print (host + " "+ "is down")
						textfile.write(host + " "+ "is down \n")
	continue_check() 
	
	
def socket_scan():
	starting_host = input("Input starting host: ")
	final_host = input("Input final host: ")
	port = input("Enter the port to scan. ")
	sh_split = starting_host.split(".") ### Splits the host IP into individual bytes###
	fh_split = final_host.split(".")
	print("###Scanning###")
	textfile = open("ping"+ " " + starting_host + "-" + final_host + ".txt", "w+")
	if sh_split[0] != fh_split[0]:
		for num in range(int(sh_split[0]),(int(fh_split[0])+1)): 
			oct0 = str(num)
			if num == int(sh_split[0]):
				for num in range(int(sh_split[1]),256):
					oct1 = (oct0 + "." + str(num))
					if num == int(sh_split[1]):
						for num in range(int(sh_split[2]),256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
					elif num == int(fh_split[1]):
						for num in range(0,int(fh_split[1])+1):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
					else :
						for num in range(0,256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
			elif num == int(fh_split[0]):
				for num in range(0,int(fh_split[0])+1):
					oct1 = (oct0 + "." + str(num))
					if num == int(sh_split[1]):
						for num in range(int(sh_split[2]),256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
					elif num == int(fh_split[1]):
						for num in range(0,int(fh_split[1])+1):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
					else :
						for num in range(0,256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
			else:
				for num in range(0,256):
					oct1 = (oct0 + "." + str(num))
					if num == int(sh_split[1]):
						for num in range(int(sh_split[2]),256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									ping(host,port,textfile)
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
					elif num == int(fh_split[1]):
						for num in range(0,int(fh_split[1])+1):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
					else :
						for num in range(0,256):
							oct2 = (oct1 + "." + str(num))
							if num == int(sh_split[2]):
								for num in range(int(sh_split[3]),256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							elif num == int(fh_split[2]):
								for num in range (0,int(fh_split[3])+1):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
							else:
								for num in range (0,256):
									host = (oct2 + "." + str(num))
									ping(host,port,textfile)
	if sh_split[0] == fh_split[0]:
		oct0 = sh_split[0]
		if sh_split[1] != fh_split[1]:
			for num in range(int(sh_split[1]),(int(fh_split[1])+1)): 
				oct1 = (oct0+ "." + str(num))
				if num == int(sh_split[1]):
					for num in range(int(sh_split[2]),256):
						oct2 = (oct1 + "." + str(num))
						if num == int(sh_split[2]):
							for num in range(int(sh_split[3]),256):
								host = (oct2 + "." + str(num))
								ping(host,port,textfile)
						elif num == int(fh_split[2]):
							for num in range (0,int(fh_split[3])+1):
								host = (oct2 + "." + str(num))
								ping(host,port,textfile)
						else:
							for num in range (0,256):
								host = (oct2 + "." + str(num))
								ping(host,port,textfile)
				elif num == int(fh_split[1]):
					for num in range(int(sh_split[2]),256):
						oct2 = (oct1 + "." + str(num))
						if num == int(sh_split[2]):
							for num in range(int(sh_split[3]),256):
								host = (oct2 + "." + str(num))
								ping(host,port,textfile)
						elif num == int(fh_split[2]):
							for num in range (0,int(fh_split[3])+1):
								host = (oct2 + "." + str(num))
								ping(host,port,textfile)
						else:
							for num in range (0,256):
								host = (oct2 + "." + str(num))
								ping(host,port,textfile)
				else :
					for num in range(0,256):
						oct2 = (oct1 + "." + str(num))
						if num == int(sh_split[2]):
							for num in range(int(sh_split[3]),256):
								host = (oct2 + "." + str(num))
								ping(host,port,textfile)
						elif num == int(fh_split[2]):
							for num in range (0,int(fh_split[3])+1):
								host = (oct2 + "." + str(num))
								ping(host,port,textfile)
						else:
							for num in range (0,256):
								host = (oct2 + "." + str(num))
								ping(host,port,textfile)
		if sh_split[1] == fh_split[1]:
			oct1 = (oct0+ "." + sh_split[1])
			if sh_split[2] != fh_split[2]:
				for num in range(int(sh_split[2]),(int(fh_split[2])+1)): 
					oct2 = (oct1 +"."+str(num))
					if num == int(sh_split[2]):
						for num in range(int(sh_split[3]),256):
							host = (oct2 + "." + str(num))
							ping(host,port,textfile)
					elif num == int(fh_split[2]):
							for num in range (0,int(fh_split[3])+1):
								host = (oct2 + "." + str(num))
								ping(host,port,textfile)
					else:
							for num in range (0,256):
								host = (oct2 + "." + str(num))
								ping(host,port,textfile)
			if sh_split[2] == fh_split[2]:
				oct2 = (oct1+ "." + sh_split[2])
				if sh_split[3] != fh_split[3]:
					for num in range (int(sh_split[3]),int(fh_split[3])+1):
						host = (oct2 + "." + str(num))
						ping(host,port,textfile)
				elif sh_split[3] == fh_split[3]:
					host = (oct2 + "." + str(num))
					ping(host,port,textfile)
	continue_check() 
	
	
def host_scan():
		host = input("Input the host: ")
		textfile = open("Port scan for " + host + ".txt", "w+")
		portList = {21:"FTP",22:"SSH",23:"Telnet",25:"SMTP",53:"DNS",80:"HTTP",110:"POP3",119:"NNTP",123:"NTP",143:"IMAP",161:"SNMP",194:"IRC",443:"HTTPS"}
		for num in sorted(portList.keys()):
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.settimeout(1)
			connect = s.connect_ex((host,num))	
			if connect == 0:
				print (colours.Green +	portList[num] + " port " +  str(num) + " is open \n")
				textfile.write(portList[num] + " port " + str(num) + " is open \n" )
			else :
				print (colours.Red + portList[num] + " port " + " " + str(num) + " " + "is closed \n")
				textfile.write(portList[num] + " port " + " " + str(num) + " " + "is closed \n" )
		continue_check()		
				
				
def continue_check():      ### Checks if the user would like to keep using the program once a ping or scan is complete ###
	answer = input("Would you like to scan anything else? Yes or No: ")
	if answer.lower() == "yes":
		os.system("cls")
		select()
	else :
		raise SystemExit
					
					

print ("###########################")
print ("# Welcome to TBC tool #")
print ("###########################\n")
select()


