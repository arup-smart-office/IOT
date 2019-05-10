import sys
sys.path.append('./api')
from api import getDesk, postDesk

ID = 1
is_occupied = False
previous_version = 0

result = getDesk(ID)
previous_version = result['data']['getDesk']['version']

variables = {'input': {'id': ID, 'expectedVersion': previous_version, 'isOccupied': is_occupied}}
result = postDesk(variables)
print(result, '<<<< result')