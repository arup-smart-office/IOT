# Import Python Libraries
import RPi.GPIO as GPIO
import time

# Define function call
def checkLight(update_light_detected):

    # Set GPIO mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)

    # Assign GPIO Pins
    GPIO_LIGHT = 21

    # Set GPIO pin direction
    GPIO.setup(GPIO_LIGHT, GPIO.IN)

    # Define callback function
    def light_callback(GPIO_LIGHT):

        # Code for if GPIO_LIGHT channel goes high
        if GPIO.input(GPIO_LIGHT):
            update_light_detected(time.time())
            print ("Light Detected!", time.time())

        # Code for if GPIO_LIGHT channel goes low
        else:
            update_light_detected(time.time())
            print("Light Detected!", time.time())
            
        #count = 0

        # Set pin to OUPUT
        #GPIO.setup(GPIO_LIGHT, GPIO.OUT)
        #GPIO.output(GPIO_LIGHT, GPIO.LOW)
        #time.sleep(0.1)

        # Change the pin back to input
        #GPIO.setup(GPIO_LIGHT, GPIO.IN)

        # Increment Count while the pin is low
        #while (GPIO.input(GPIO_LIGHT) == GPIO.LOW):
            #count += 1

        # When the pin goes high, return the count variable
        #return count/100000

    # Add event detect function to detect rising or falling edge
    GPIO.add_event_detect(GPIO_LIGHT, GPIO.BOTH, bouncetime=300)

    # Add a threaded callback function
    GPIO.add_event_callback(GPIO_LIGHT, light_callback)

    # Catch when script is interrupted by user
    try:

        print ("Light Component Test (Ctrl + C to exit)")
        time.sleep(1)
        print ("Light Component Ready!")
        
        # Main loop
        #while True:

            # This will print the count variable when returned
            #print (str(light_callback(GPIO_LIGHT)) + " seconds", time.time())

    except KeyboardInterrupt:
        print ("Quitting Light Component")

        # Cleanup GPIO Input pins
        GPIO.cleanup()

#checkLight(lambda x: (x))

#while True:
    #time.sleep(0.1)
