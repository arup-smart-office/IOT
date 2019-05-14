# Import Python Libraries
import RPi.GPIO as GPIO
import time

print ("Running Sound DEtector Component")

# Define function call
def checkSound(update_sound_detected):
    
    # Setup GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)

    # Assign GPIO PINS
    GPIO_SOUND = 22

    # Set GPIO Pin Direction
    GPIO.setup(GPIO_SOUND, GPIO.IN)

    # Define a threaded callback function
    def sound_callback(GPIO_SOUND):

        # Code for if GPIO_SOUND channel goes high
        if GPIO.input(GPIO_SOUND):
            update_sound_detected(time.time())
            print ("Sound Detected", time.time())

        # Code for if GPIO_SOUND channel goes low
        else:
            update_sound_detected(time.time())
            print ("Sound Detected", time.time())

    # Add event detect function to detect rising or falling edge
    GPIO.add_event_detect(GPIO_SOUND, GPIO.BOTH, bouncetime=300)

    # Add threaded callback funcction
    GPIO.add_event_callback(GPIO_SOUND, sound_callback)

    # Attempt code in try block
    try:

        print ("SOUND Detector Module Test (Ctrl + C to exit)")
        time.sleep(2)
        print ("SOUND Detector Ready")

    # Execute code within except block
    except KeyboardInterrupt:
        print ("Quitting Sound Detector Module")

        # Cleanup GPIO Pins
        GPIO.cleanup()

#checkSound(lambda x: (x))

#while True:
    #time.sleep(0.1)
