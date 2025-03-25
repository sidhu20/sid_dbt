# rest api implementation

# import of lib

import requests
# import pandas as pd

# endpoint 
api_endpoint = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

# make a api request to extract the data 
api_request = requests.get(api_endpoint)

# capture the response as json 
api_response = api_request.json()

print(api_response)

