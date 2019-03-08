import pymysql.cursors

db = pymysql.connect("jamesbraman.com.ipagemysql.com", "weatherpi","123!weatherR", "weather")

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)

# disconnect from server
db.close()

# set sql variable to sql query
sql = "INSERT INTO MAIN(PINUMBER, LOCATION, TEMPTIME, TEMP, HUMTIME, HUMIDITY) VALUES (1,US,1300,32,1300,0)"

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()