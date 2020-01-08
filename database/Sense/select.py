import pymysql
import sys
import datetime

try:

    db = pymysql.connect(

      host= '192.168.1.15',

      user= 'pi',

      passwd= '!QAZ@WSX1qaz2wsx',

      db= 'weatherDB')

    cursor=db.cursor()
    print("connected to the database")

    select = "SELECT DateTime FROM Weather;"
    dates=cursor.execute(select)

    select = "SELECT Temperature FROM Weather;"
    temperatures = cursor.execute(select)

    temps = cursor.fetchall()

    for i in temps:
        print(i)
        

    select = "SELECT Humidity FROM Weather;"
    humidity = cursor.execute(select)

    print("Records retrieved successfully")

except pymysql.Error as e:

    print("Error %d: %s" % (e.args[0], e.args[1]))

    sys.exit(1)

