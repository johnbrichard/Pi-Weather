from flask import Flask, render_template
import time
import Adafruit_DHT

#---set sensor to variable named sensor
sensor=Adafruit_DHT.DHT11
#---set gpio variable to pin 17
gpio=17

#initiates app object for our application
app = Flask(__name__)

#designates where the web app is located
@app.route('/')

def index():
    #---set date_time variable to date and time of OS
    local_time = time.asctime(time.localtime(time.time()))
    #---read data from sensor and assign to humidity and temperature variables
    hum, temp = Adafruit_DHT.read_retry(sensor, gpio)
    #---converts temperature to fahrenheit
    temp=((temp*9/5)+32)
    #returns the sensor data and populates it into the index.html file
    return render_template('index.html', time=local_time, temperature=temp, humidity=hum)

if __name__ == '__main__':
        #launches the Flask application and makes it available to everyone
        #on the designated network
        app.run(debug=True, host='0.0.0.0')
        
