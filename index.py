import sys
import time
sys.path.append('./api')
sys.path.append('./Components')
from api import getDesk, postDesk

import sound

import temp_humid

ID = 1
is_occupied = False
previous_version = 0

result = getDesk(ID)

previous_version = result['data']['getDesk']['version']

while True:
    #sound()
    #pir()
    temp_humid()
    time.sleep(2)

#variables = {'input': {'id': ID, 'expectedVersion': previous_version, 'isOccupied': is_occupied}}
#result = postDesk(variables)
