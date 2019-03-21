import time
from sense_hat import SenseHat

#---sets SenseHat to variable sense and clears sensor
sense = SenseHat()
sense.clear()

#---sets loop to print sensor data
while True:
    #---set date_time variable to date and time of OS
    local_time = time.asctime(time.localtime(time.time()))
    
    #---read data from Sense Hat and assign to appropriate variables
    temperature='%2d'% (((sense.get_temperature())*9/5)+32)
    humidity = '%2d'% sense.get_humidity()
    pressure = '%2d'% sense.get_pressure()
    
    #---prints data from sensor
    print(local_time, temperature, humidity)
    
    #---sets time delay to 5 seconds
    time.sleep(5)
