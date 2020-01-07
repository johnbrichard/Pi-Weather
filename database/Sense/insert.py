import pymysql
import sys
import datetime
from sense_hat import SenseHat

try:
    sense = SenseHat()
    sense.clear()

    db = pymysql.connect(

      host= '192.168.1.15',

      user= 'pi',

      passwd= '!QAZ@WSX1qaz2wsx',

      db= 'weatherDB')

    cursor=db.cursor()
    print("connected to the database")

    time = datetime.datetime.now()
    humidity='%2d'% sense.get_humidity()
    temperature='%2d'% (((sense.get_temperature())*9/5)+32)

    insert = "INSERT INTO `Weather` (`DateTime`, `Temperature`, `Humidity`) VALUES (%s, %s, %s)"

    cursor.execute(insert,(time, temperature, humidity))
    db.commit()
    print("Record inserted successfully")

except pymysql.Error as e:

    print("Error %d: %s" % (e.args[0], e.args[1]))

    sys.exit(1)

