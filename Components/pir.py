# Import Python Libraries
import RPi.GPIO as GPIO
import time


print ("Running PIR Sensor Component")

# Define function call
def checkMotion(update_pir_motion):
    
    # Set GPIO mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)

    # Assign input pin
    GPIO_PIR = 4

    # Set GPIO Direction
    GPIO.setup(GPIO_PIR, GPIO.IN)

    # Define a threaded callback function
    def pir_callback(GPIO_PIR):

        # Code for if GPIO_PIR channel goes high
        if GPIO.input(GPIO_PIR):
            update_pir_motion(time.time())
            print ("Motion Detected!", time.time())

        # Code for if GPIO_PIR channel goes low
        else:
            update_pir_motion(time.time())
            print ("Motion Detected!", time.time())

    # Add event detect function to detect rising or falling edge
    GPIO.add_event_detect(GPIO_PIR, GPIO.BOTH, bouncetime=300)

    # Add threaded callback function
    GPIO.add_event_callback(GPIO_PIR, pir_callback)

    # Attempt code within try block
    try:
        
        print ("PIR Module Test (Crtl + C to exit)")
        time.sleep(2)
        print ("PIR Component Ready")

    # Execute code within except block
    except KeyboardInterrupt:
        print ("Quitting PIR Component")

        # Cleanup GPIO Input pins
        GPIO.cleanup()

#checkMotion(lambda x: (x))
            
#while True:
    #time.sleep(0.1)
    
