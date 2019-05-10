# Import Python Libraries
import RPi.GPIO as GPIO
import time

# Set GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Assign GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

# Set GPIO Direction for Pins
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Define Trigger Function
def distance():

    # Set Trigger Pin to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # Set sleep timer and Toggle Trigger Pin
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIGGER, False)

    # Define variables for start and end of signal transmission
    StartTime = time.time()
    StopTime = time.time()

    # Save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # Save time of signal arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # Calculate time difference
    TimeElapsed = StopTime - StartTime

    # Calculate distance using sonic speed (34300 cm/s)
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
