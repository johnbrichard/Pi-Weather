import pymysql.cursors

connection = pymysql.connect(host='jamesbramancom.ipagemysql.com',
                             user='weatherpi',
                             password='123!weatherR',
                             db='weather',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        # set sql variable to sql query
        sql = "INSERT INTO `main`(`pinnumber`, `location`, `temptime`, `temp`, `humtime`, `humidity`) VALUES (1,US,1300,32,1300,0)"
        #sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql1 = "SELECT `temp`, `humidity` FROM `main` WHERE `temptime`=1300"
        cursor.execute(sql1)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
