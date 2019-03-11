import mysqldba
import sys

print("Content-type:text/html\n\n")

try:

    conn = mysqldba.connect(

        host="jamesbramancom.ipagemysql.com",

        user="weatherpi",

        passwd="123!weatherR",

        db="weather")

    print("connected to the database")

except MySQLdb.Error as e:

    print("Error %d: %s" % (e.args[0], e.args[1]))

    sys.exit(1)

