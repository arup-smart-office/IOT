# Import Python Libraries
import RPi.GPIO as GPIO
import dht11
import time
import datetime

# Initialise GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Read data using GPIO Pin
instance = dht11.DHT11(pin=27)

while True:
    result = instance.read()
    if result.is_valid():
        print ("Last valid input: " + str(datetime.datetime.now()))
        print ("Temperature: %d C" % result.temperature)
        print ("Humidity: %d %%" % result.humidity)

    time.sleep(1)

