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
import json

#initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#---set date_time variable to date and time of OS
date_time = datetime.datetime.now()

#---depending on if the file exists within the specified path
file_exists = os.path.isfile(file_name)

# read data using pin 14
instance = dht11.DHT11(pin=17)

# set data to variable
result = instance.read()
data = {
        "weather": {
            "time": date_time,
            "temperature": (((result.temperature)*9/5)+32),
            "humidity": result.humidity
                    }
        }

#---tests if log_file exists
if file_exists==True:

    #---if log file alread exists it will append with sensor data
    with open("data_file.json", "a") as write_file:
        json.dump(data, write_file, default=str)

else:
    
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file, default=str)
