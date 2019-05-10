import requests
from aws_exports import awsmobile

headers = {"x-api-key": awsmobile["aws_appsync_apiKey"]}

def postDesk(variables):
  query = """
  mutation UpdateDesk($input: UpdateDeskInput!) {
    updateDesk(input: $input) {
      id
      isOccupied
      version
	  }
  }
  """
  request = requests.post(awsmobile["aws_appsync_graphqlEndpoint"], json={'query': query, 'variables': variables}, headers=headers)
  print(request, '<<< request')
  print(request.status_code, '<<<< status code')
  if request.status_code == 200:
    return request.json()


def getDesk(id):
  print(id)
  query = """
  query GetDesk($id: ID!) {
    getDesk(id: $id) {
      version
	  }
  }
  """
  request = requests.post(awsmobile["aws_appsync_graphqlEndpoint"], json={'query': query, 'variables': {'id': id}}, headers=headers)
  if request.status_code == 200:
    return request.json()

