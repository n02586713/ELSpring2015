import sqlite3
import os
import time
conn=sqlite3.connect('temperature.db')
c=conn.cursor()
def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-000006962ba7/w1_slave")
	tempfile_text = tempfile.read()
	currentTime=time.strftime('%x %X %Z')
	tempfile.close()
	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF=tempC*9.0/5.0+32.0
	print "current temperature is: " + str(tempF) + " F"
	params=(currentTime,tempC,tempF)
	c.execute("INSERT INTO TempData VALUES (?, ?, ?)", (currentTime, tempC, tempF))
	conn.commit()
	return [currentTime, tempC, tempF]

#conn=sqlite3.connect('temperature.db')
#c= conn.cursor()

#def tableCreate():
#	c.execute("CREATE TABLE TempData(currentTime text, tempC double, tempF double)")
#	conn.commit()
#def dataEntry():
#	params=(currentTime, tempC, tempF)
#	c.execute("INSERT INTO TempData VALUES(NULL, ? , ?, ?)",params)
#	conn.commit()


def get_posts():
	#c.execute(".mode column")
	#conn.commit()
	c.execute("SELECT * FROM TempData")
	conn.commit()
	print(c.fetchall())
	
#tableCreate()
readTemp()
#dataEntry()
#get_posts()


print "Temperature logged"
