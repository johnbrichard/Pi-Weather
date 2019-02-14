#	This script will check for a log file for sensor data. 
#	If log file exists, it will append with new sensor data 
#	(to include date and time as given by the OS.) 
#	If log file does not exist, it will create a new file 
#	and add a title.

import os
import datetime

#---set date_time variable to date and time of OS
date_time = datetime.datetime.now()

#---set file_name variable to match output file name
file_name = 'test.txt'

#---sets log_file variable to boolean (T/F) 
#---depending on if the file exists within the specified path
log_file = os.path.isfile(file_name)

#---tests if log_file exists
if log_file==True:
	    
    #---if log file alread exists it will append with sensor data
    log_file = open(file_name, "a")
    log_file.write('\n')
    log_file.write(str(date_time))
    log_file.write('\nTemperature: 40C   Humidity: 100%\n')
	
else:

    #---if log file does not exist, creates new log file
    #---and adds title line so file is not empty
    log_file = open("test.txt", "w")
    log_file.write("Test file\n")
	
log_file.close()