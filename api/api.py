import requests
from aws_exports import awsmobile

headers = {"x-api-key": awsmobile["aws_appsync_apiKey"]}

def postData(query):
    request = requests.post(awsmobile["aws_appsync_graphqlEndpoint"], json={'query': query}, headers=headers)
    print(request, '<<< request')
    print(request.status_code, '<<<< status code')
    if request.status_code == 200:
      return request.json()

query = """
  mutation {
    updateDesk(input: {id:1, expectedVersion:14 isOccupied:true}) {
      id
      isOccupied
      version
	  }
  }
"""

result = postData(query)
print(result, '<<<< result')