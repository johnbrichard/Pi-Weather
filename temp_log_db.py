print ("Content-type:text/html\n\n")

import mysqldb
#import RPi.GPIO as GPIO
import datetime
#import dht11
import PyMySQL

#initialize GPIO
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

db = pymysql.connect("jamesbraman.com.ipagemysql.com", "weatherpi","123!weatherR", "main")

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()
#read data using pin 14
#instance = dht11.DHT11(pin=17)
#set data to variable
#result = instance.read()
#set variables to pass to the database
#temperature=(((result.temperatere)*9/5)+32)
#humidity=result.humidity
#date_time=datetime.datetime.now()

# set sql variable to sql query
#sql = ("INSERT INTO MAIN(PINUMBER, LOCATION, TEMPTIME, TEMP, HUMTIME, HUMIDITY) VALUES (1,US,",date_time,",",temperature,",",date_time,",",humidity,")")
#sql = "INSERT INTO MAIN(PINUMBER, LOCATION, TEMPTIME, TEMP, HUMTIME, HUMIDITY) VALUES (1,US,1300,32,1300,0)"

#try:
#    cursor.execute(sql)
#    db.commit()
#except:
#    db.rollback()

#db.close()

#try:
#
#   conn = MySQLdb.connect (
#
#     host = "jamesbramancom.ipagemysql.com",
#
#      user = "weatherpi",
#
#      passwd = "123!weatherR",
#
#      db = "weather")
#
#except MySQLdb.Error, e:
#
#    print "Error %d: %s" % (e.args[0], e.args[1])
#
#    sys.exit (1)

 

#print "connected to the database"



