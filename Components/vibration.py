# Import Python Libraries
import RPi.GPIO as GPIO
import time

# Set GPIO mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Assign input pin
GPIO_VIBRATION = 17

# Set GPIO Direction
GPIO.setup(GPIO_VIBRATION, GPIO.IN)

print ("Running Vibration Sensor Component")

# Define function call
def checkVibration(update_vibration_motion):

    # Define a threaded callback function
    def vibration_callback(GPIO_VIBRATION):

        # Code for if GPIO_VIBRATION channel goes high
        if GPIO.input(GPIO_VIBRATION):
            update_vibration_motion(time.time())
            print ("Vibration Detected!", time.time())

        # Code for if GPIO_VIBRATION channel goes low
        else:
            update_vibration_motion(time.time())
            print ("Vibration Detected!", time.time())

    # Add event detect function to detect rising or falling edge
    GPIO.add_event_detect(GPIO_VIBRATION, GPIO.BOTH, bouncetime=300)

    # Add threaded callback function
    GPIO.add_event_callback(GPIO_VIBRATION, vibration_callback)

    # Attempt code within try block
    try:

        print ("Vibration Sensor Module Test (Ctrl + C to exit)")
        time.sleep(2)
        print ("Vibration Component Ready!")

    # Execute code within except block
    except KeyboardInterrupt:
        print ("Quitting Vibration Component")

        # Cleanup GPIO Input pins
        GPIO.cleanup()

#checkVibration(lambda x:(x))

#while True:
    #time.sleep(0.1)
