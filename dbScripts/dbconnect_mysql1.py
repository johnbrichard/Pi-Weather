import mysql
from mysql.connector import Error
from mysql.connector import errorcode

try:

    connection = mysql.connector.connect(host='localhost',
                 database='csit216',
                 user='root',
                 password='!QAZ@WSX1qaz2wsx')

    sql_insert_query = """ INSERT INTO `weather`
                       (`id`, `temp`, `humidity`, `time`)
                       VALUES (1,93,35, '2018-04-11')"""

    cursor = connection.cursor()
    result  = cursor.execute(sql_insert_query)
    connection.commit()

    print ("Record inserted successfully into python_users table")

except mysql.connector.Error as error :

    connection.rollback() #rollback if any exception occured

    print("Failed inserting record into python_users table {}".format(error))

finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
