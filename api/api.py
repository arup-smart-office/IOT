import requests
from aws_exports import awsmobile

ID = 1
previous_version = 16
is_occupied = False

headers = {"x-api-key": awsmobile["aws_appsync_apiKey"]}

def postData(query, variables):
    request = requests.post(awsmobile["aws_appsync_graphqlEndpoint"], json={'query': query, 'variables': variables}, headers=headers)
    print(request, '<<< request')
    print(request.status_code, '<<<< status code')
    if request.status_code == 200:
      return request.json()

query = """
  mutation UpdateDesk($input: UpdateDeskInput!) {
    updateDesk(input: $input) {
      id
      isOccupied
      version
	  }
  }
"""
variables = {'input': {'id': ID, 'expectedVersion': previous_version, 'isOccupied': is_occupied}}

result = postData(query, variables)
print(result, '<<<< result')