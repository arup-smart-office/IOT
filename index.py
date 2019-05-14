# Import Python Libraries
import RPi.GPIO as GPIO
import sys
import time
import numpy

# Add file directory paths to allow import from other locations
sys.path.append('./api')
sys.path.append('./Components')

# Import functions for api call
from api import getDesk, postDesk

# Import functions from sensor components
from pir import checkMotion
from vibration import checkVibration
from ultrasonic_distance import checkDistance
from temp_humid import checkTempAndHumid
from sound import checkSound

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Create JSON data object for api call
ID = 1
is_occupied = False
previous_version = 0

# Make api call to get desk information for desk ID
result = getDesk(ID)
previous_version = result['data']['getDesk']['version']

# Define empty array / list for distance measuements
distance_measurements = []

# Invoke desk occupancy functions
pir_motion = None
pir_motion_activated = False

# Define function to store timestamp of PIR sensor trigger
def update_pir_motion(time):
        global pir_motion
        global pir_motion_activated
        pir_motion = time
        pir_motion_activated = True
checkMotion(update_pir_motion)

# Define function to store timestamp of Vibration Sensor trigger
vibration_motion = None
vibration_motion_activated = False
def update_vibration_motion(time):
        global vibration_motion
        global vibration_motion_activated
        vibration_motion = time
        vibration_motion_activated = True
checkVibration(update_vibration_motion)

temperature_reading = None
def update_temperature_reading(time):
        global temperature_Reading
        temperature_reading = time

humidity_reading = None
def update_humidity_reading(time):
        global humidity_reading
        humidity_reading = time

sound_detected = None
sound_detector_activated = False
def update_sound_detected(time):
        global sound_detected
        global sound_detector_activated
        sound_detected = time
        sound_detector_activated = True
checkSound(update_sound_detected)

# Enter indefinite loop for sensor components
while True:

        checkTempAndHumid(update_temperature_reading, update_humidity_reading)
        
	print ("Measured Distance = %.1f cm" % checkDistance())

        # Append new distance measurements to the array
        distance_measurements.append(checkDistance())
        # print(distance_measurements)

        # Test if 30 distance readings have been made
	if len(distance_measurements) > 30:


                # Calculate statistics for values in distance measurements data
                average_distance = numpy.average(distance_measurements)
                max_distance = max(distance_measurements)
                min_distance = min(distance_measurements)
                delta_distance = numpy.diff(distance_measurements)

                #print (delta_distance)

                distance_activated = False

                delta_filtered_distance = filter(lambda x: (x > 1), delta_distance)

                #delta_filtered_distance.pop(0)

                active_desk_distance = filter(lambda x: (x < 100), distance_measurements)

                #print (delta_distance,"<<--DELTA")
                #print (delta_filtered_distance,"<<--FILTERED")

                if (len(delta_filtered_distance) > 10 and len(active_desk_distance) > 8):
                        distance_activated = True

                is_occupied = (vibration_motion_activated\
                               and pir_motion_activated\
                               and distance_activated)

                print (vibration_motion_activated, "<<-- VIBRATION")
                print (pir_motion_activated, "<<--MOTION")
                print (distance_activated, "<<--DISTANCE")
                print (is_occupied,"<<-- DESK_OCCUPANCY")
                
                # Make API call to database
                #variables = {'input': {'id': ID, 'expectedVersion': previous_version, 'isOccupied': is_occupied}}
                #result = postDesk(variables)
                #print (result)
                #print (previous_version)
                #previous_version = result['data']['updateDesk']['version']
                #print (previous_version)

                # Clear distance measurements array and set Vibration and Motion sensors to false
                vibration_motion_activated = False
                pir_motion_activated = False
                distance_measurements = []

                #print (average_distance, max_distance, min_distance)
		
	time.sleep(1)
