# Import Python Libraries
import RPi.GPIO as GPIO
import time

# Set GPIO mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Assign GPIO Pins
GPIO_LIGHT = 21

# Define callback function
def rc_time(GPIO_LIGHT):
    count = 0

    # Set pin to OUPUT
    GPIO.setup(GPIO_LIGHT, GPIO.OUT)
    GPIO.output(GPIO_LIGHT, GPIO.LOW)
    time.sleep(0.1)

    # Change the pin back to input
    GPIO.setup(GPIO_LIGHT, GPIO.IN)

    # Increment Cout while the pin is low
    while (GPIO.input(GPIO_LIGHT) == GPIO.LOW):
        count += 1

    # When the pin goes high, return the count variable
    return count/100000

# Catch when script is interrupted by user
try:
    # Main loop
    while True:
        # This will print the count variable when returned
        print (str(rc_time(GPIO_LIGHT)) + " seconds")
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
