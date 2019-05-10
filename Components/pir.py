# Import Python Libraries
import RPi.GPIO as GPIO
import time

# Set GPIO mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Assign input pin
GPIO_PIR = 4

# Set GPIO Direction
GPIO.setup(GPIO_PIR, GPIO.IN)

# Add time delay
try:
    print ("PIR Module Test (Crtl + C to exit)")
    time.sleep(2)
    print ("Ready")

    # Check status of PIR pin on loop
    while True:
        if GPIO.input(GPIO_PIR):
            print ("Motion Detected!")
        time.sleep(1)

except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()
