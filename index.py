# Import Python Libraries
import sys
import time

# Add file directory paths to allow import from other locations
sys.path.append('./api')
sys.path.append('./Components')

# Import functions for api call
from api import getDesk, postDesk

# Import functions from sensor components
from pir import checkMotion
from vibration import checkVibration
from ultrasonic_distance import checkDistance

# Create JSON data object for api call
ID = 1
is_occupied = False
previous_version = 0

# Make api call to get desk information for desk ID
result = getDesk(ID)

previous_version = result['data']['getDesk']['version']

# Invoke desk occupancy functions
checkMotion()
checkVibration()

# Enter indefinite loop for sensor components
while True:

	print ("Measured Distance = %.1f cm" % checkDistance())
	time.sleep(2)
	

#variables = {'input': {'id': ID, 'expectedVersion': previous_version, 'isOccupied': is_occupied}}
#result = postDesk(variables)
