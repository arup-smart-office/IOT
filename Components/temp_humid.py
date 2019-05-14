# Import Python Libraries
import RPi.GPIO as GPIO
import dht11
import time
import datetime


print ("Running Temperature and Humidity component")

# Define function call
def checkTempAndHumid(update_temperature_reading, update_humidity_reading):

    # Initialise GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
    # Assign GPIO input pin
    GPIO_TempAndHumid = 27

    # Set GPIO pin direction
    GPIO.setup(GPIO_TempAndHumid, GPIO.IN)

    # Read data using GPIO Pin
    instance = dht11.DHT11(pin=GPIO_TempAndHumid)

    # Read result data from DHT11 sensor
    result = instance.read()
    if result.is_valid():
            
        update_temperature_reading(result.temperature)
        update_humidity_reading(result.humidity)
            
        print ("Last valid input: " + str(datetime.datetime.now()))
        print ("Temperature: %d C" % result.temperature)
        print ("Humidity: %d %%" % result.humidity)


    # Add event detect function to detect rising or falling edge
    #GPIO.add_event_detect(GPIO_TempAndHumid, GPIO.BOTH, bouncetime=300)

    # Add threaded callback function
    #GPIO.add_event_callback(GPIO_TempAndHumid, tempAndHumid_callback)

        
