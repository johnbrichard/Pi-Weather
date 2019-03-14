from flask import Flask, render_template
import RPi.GPIO as GPIO
from datetime import date
import time
import dht11

#sets our GPIO pins to read data fed into them
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#initiates instance variable which points to our DHT11 sensor
instance = dht11.DHT11(pin=17)

#initiates app object for our application
app = Flask(__name__)

#designates where the web app is located
@app.route('/')

def index():
    #reads data from DHT11
    result = instance.read()
    #returns the sensor data and populates it into the index.html file
    return render_template('index.html', time=time.asctime( time.localtime(time.time()) ), date= date.today() ,temperature=(((result.temperature)*9/5)+32), humidity=result.humidity)

if __name__ == '__main__':
        #launches the Flask application and makes it available to everyone
        #on the designated network
        app.run(debug=True, host='0.0.0.0')
        
