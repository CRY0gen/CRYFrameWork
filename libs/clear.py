import os
import platform

def clear():
	OS=platform.system()
	if OS=="Windows":
		os.system("CLS")
	else:
		os.system("clear")

if __name__=="__main__":
	clear()
