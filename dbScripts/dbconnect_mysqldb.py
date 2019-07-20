import MySQLdb
import sys
import time
import Adafruit_DHT

try:
    sensor=Adafruit_DHT.DHT11

    gpio=17

    db = MySQLdb.connect(

      host= "96.244.106.43",

      user= "user",

      passwd= "Pa$$word12345",

      db= "csit216")

    cursor=db.cursor()
    print("connected to the database")

    local_time = time.asctime(time.localtime(time.time()))
    humidity, temperature = Adafruit_DHT.read_retry(sensor,gpio)
    temperature=((temperature*9/5)+32)

    insert = "INSERT INTO `weather` (`date`, `temperature`, `humidity`) VALUES (%s, %s, %s)"

    cursor.execute(insert,(local_time, temperature, humidity))
    db.commit()
    print("Record inserted successfully")

except MySQLdb.Error as e:

    print("Error %d: %s" % (e.args[0], e.args[1]))

    sys.exit(1)

