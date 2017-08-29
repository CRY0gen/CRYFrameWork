#Needed libs

import time
import os
import sys

#Defining Globals and Costants

DEF_LOG_DIR="/logs/"
LOG_NAME="CRYxx.xx.xx.log" #where xx.xx.xx is the date
err="[ERROR]"
warn="[WARNING]"
deb="[DEBUG]"
outp="[OUTPUT]"

##Defining Functions

class CRYLog:
	def __init__(self, dir):
		self.filename=None
		self.filedir=dir
		date = {
			"day" : str(time.gmtime(time.time()).tm_mday),
			"month" : str(time.gmtime(time.time()).tm_mon),
			"year" : str(time.gmtime(time.time()).tm_year)
		}
		self.createLogFile(date)
	def createLogFile(self,date):
		self.filename="CRY"+date["day"]+"."+date["month"]+"."+date["year"]+".log"
		##First of All It'll check file existance
		try:
			f=open(self.filedir+"/"+self.filename,"r")
			fcont=f.read()
			fcont+="\n"+"------------------------------------------------"
			f.close()
			f=open(self.filedir+"/"+self.filename,"w")
			f.write(fcont)
			f.close()
		except:
			print("[!]No logfile detected,creating one...")
			try:
				os.system("echo \"-------------------\" > " + self.filedir + "/" + self.filename)
			except:
				print("[!]Could not create file!\nAborting...")
				exit()
	def CRYprint(self, data, log=True):
		if log == True:
			f=open(self.filedir+"/"+self.filename, "r")
			fcont=f.read()
			fcont+="\n"
			fcont+=outp + " " + data
			f.close()
			f=open(self.filedir+"/"+self.filename, "w")
			f.write(fcont)
			f.close()
		print(data)
	def CRYlog(self, data, typedata):
		f=open(self.filedir+"/"+self.filename, "r")
		fcont=f.read()
		fcont+="\n" + typedata + " " + data
		f.close()
		f=open(self.filedir + "/" + self.filename, "w")
		f.write(fcont)
		f.close()

if __name__=="__main__":
	CRLOG=CRYLog("../CRYData/CRYlogs")
	printc=CRLOG.CRYprint
	clog=CRLOG.CRYlog
	printc("This hopefully will be logged")
	clog("Test Message", deb)
