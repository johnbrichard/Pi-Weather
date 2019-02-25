from sense_hat import SenseHat
import os
import datetime
import time

sense = SenseHat()

# Define the colours red and green
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# ---set date_time variable to date and time of OS
date_time = datetime.datetime.now()

# set data to variable
# Take readings from all three sensors
t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()

# Round the values to one decimal place
t = round(t, 1)
p = round(p, 1)
h = round(h, 1)

# ---set file_name variable to match output file name
file_name = 'Mike_log.txt'

# ---sets log_file variable to boolean (T/F)
# ---depending on if the file exists within the specified path
file_exists = os.path.isfile(file_name)

# ---tests if log_file exists
if file_exists:

    # check to see that data is valid
    # output data
    # print("Last valid input: " + str(datetime.datetime.now()))
    # print("Temperature: %d C" % result.temperature)
    # print("Temperature: %d F" % (((result.temperature)*9/5)+32))
    # print("Humidity: %d %%" % result.humidity)

        # ---if log file already exists it will append with sensor data
        log_file = open(file_name, "a")
        log_file.write('\n' + str(date_time)
                        + '\nTemperature: %d F ' % (t * (9 / 5) + 32)
                        + 'Humidity: %d %%' % h + ' Pressure: %d millibars' % p)
        log_file.close()

else:

    # ---if log file does not exist, creates new log file
    # ---and adds title line so file is not empty
    log_file = open("Mike_log.txt", "w")
    log_file.write("Temperature log file\n")
    log_file.close()

print (t)
print (h)
print (p)
# Create the message
# str() converts the value to a string so it can be concatenated
# message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

# if 18.3 < t < 26.7:
#       bg = green
#  elif t >= 26.7:
#      bg = red
#       elif t <= 18.3
#           bg = blue

# Display the scrolling message
# sense.show_message(message, scroll_speed=0.05, back_colour=bg)
