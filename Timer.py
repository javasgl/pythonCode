#!/usr/bin/env python3
#-*-encoding:utf8-*-


import threading

def func():
	print "timer"

timer=threading.Timer(5,func)
timer.start()



while True:
	timer=threading.Timer(5,func)
	# timer.start()

for i in [1,2,3,4,5,6]:
	print i
