import time
import Adafruit_DHT

#---set sensor to variable named sensor
sensor=Adafruit_DHT.DHT11
#---set gpio variable to pin 17
gpio=17

#---sets loop to print sensor data
while True:
    #---set date_time variable to date and time of OS
    local_time = time.asctime(time.localtime(time.time()))
    #---read data from sensor and assign to humidity and temperature variables
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    #---converts temperature to fahrenheit
    temperature=((temperature*9/5)+32)
    #---prints data from sensor
    print(local_time, temperature, humidity)
    #---sets time delay to 5 seconds
    time.sleep(5)
