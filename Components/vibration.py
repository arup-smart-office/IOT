# Import Python Libraries
import RPi.GPIO as GPIO
import time

# Set GPIO mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Assign input pin
GPIO_VIBRATION = 17

# Set GPIO Direction
GPIO.setup(GPIO_VIBRATION, GPIO.IN)

# Define Callback Function
def callback(GPIO_VIBRATION):
    if GPIO.input(GPIO_VIBRATION):
        print ("Movement Detected!")
    else:
        print ("Movement Detected!")

GPIO.add_event_detect(GPIO_VIBRATION, GPIO.BOTH, bouncetime=300)

GPIO.add_event_callback(GPIO_VIBRATION, callback)

while True:
    time.sleep(1)

