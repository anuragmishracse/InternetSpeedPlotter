import matplotlib.pyplot as plt
import requests
import datetime
import time
import csv

url="https://androidnetworktester.googlecode.com/files/1mb.txt"

min_sec = 0

i=0
x=[]
y=[]

while(time.asctime()[4:]<="Nov 21 15:35:00 2014"):
	
	cur_sec = time.time()
	
	if(cur_sec-min_sec >= 300):
		min_sec=cur_sec
		x.append(datetime.datetime.now())
		
		print "Download ",i, "start"	
		time1=time.time()

		try:		
			r=requests.get(url)
		except:
			print "Exception"
			continue
		time2=time.time()
		time_taken=time2-time1
		print "Finished downloading ",i

		print "Time taken : ",time_taken," seconds"
		
		speed=1024/time_taken
		y.append(speed)
		i+=1
		print"\n"

print x,y
plt.xlabel('start time')
plt.ylabel('speed in KBps')
plt.plot(x,y)
plt.show()
	
