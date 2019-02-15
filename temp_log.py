#	This script will check for a log file for sensor data. 
#	If log file exists, it will append with new sensor data 
#	(to include date and time as given by the OS.) 
#	If log file does not exist, it will create a new file 
#	and add a title.

import RPi.GPIO as GPIO
import os
import datetime
import dht11
import time

#initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#---set date_time variable to date and time of OS
date_time = datetime.datetime.now()

#---set file_name variable to match output file name
file_name = 'temp_log.txt'

#---sets log_file variable to boolean (T/F) 
#---depending on if the file exists within the specified path
file_exists = os.path.isfile(file_name)

#---tests if log_file exists
if file_exists==True:

    # read data using pin 14
    instance = dht11.DHT11(pin=17)

    # set data to variable
    result = instance.read()
    
    #check to see that data is valid
    if result.is_valid():
	
	# output data
        #print("Last valid input: " + str(datetime.datetime.now()))
        #print("Temperature: %d C" % result.temperature)
	#print("Temperature: %d F" % (((result.temperature)*9/5)+32))
        #print("Humidity: %d %%" % result.humidity)

	#---if log file alread exists it will append with sensor data
	log_file = open(file_name, "a")
	log_file.write('\n' +str(date_time) 
		 	+'\nTemperature: %d F '% (((result.temperature)*9/5)+32)  
			+'Humidity: %d %%' % result.humidity) 
	log_file.close()

else:

    #---if log file does not exist, creates new log file
    #---and adds title line so file is not empty
    log_file = open("temp_log.txt", "w")
    log_file.write("Temperature log file\n")
    log_file.close()
