#	This script will check for a data_file.json for sensor data.
#	If log file exists, it will append with new sensor data 
#	(to include date and time as given by the OS.) 
#	If log file does not exist, it will create a new file 
#	and add a title.
import os
import time
import Adafruit_DHT
import json

#---set sensor to variable named sensor
sensor=Adafruit_DHT.DHT11
#---set gpio variable to pin 17
gpio=17
#---set date_time variable to date and time of OS
local_time = time.asctime(time.localtime(time.time()))

#---read data from sensor and assign to humidity and temperature variables
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
#---converts temperature to fahrenheit
temperature=((temperature*9/5)+32)

#---sets file_exists to path of json file
file_exists = os.path.isfile('data_file.json')

# set data to variable
data = {
        "weather": {
            "time": local_time,
            "temperature": temperature,
            "humidity": humidity
                    }
        }

#---tests if log_file exists
if file_exists==True:

    #---if log file alread exists it will append with sensor data
    with open("data_file.json", "a") as write_file:
        json.dump(data, write_file, default=str)

else:
    #---if log file doesn't exist it will be created and sensor data added
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file, default=str)
