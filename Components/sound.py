# Import Python Libraries
import RPi.GPIO as GPIO
import time

# Setup GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Assign GPIO PINS
GPIO_SOUND = 22

# Set GPIO Pin Direction
GPIO.setup(GPIO_SOUND, GPIO.IN)

# Define Callback Function
def callback(GPIO_SOUND):
    if GPIO.input(GPIO_SOUND):
        print ("Sound Detected")
    else:
        print ("Sound Detected")

GPIO.add_event_detect(GPIO_SOUND, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(GPIO_SOUND, callback)

while True:
    time.sleep(1)
