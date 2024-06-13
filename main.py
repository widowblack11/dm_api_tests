"""
curl -X 'PUT' \
  'http://5.63.153.31:5051/v1/account/d7f606a3-5ed6-49ba-a6d7-5dc2f252f8c2' \
  -H 'accept: text/plain'
"""
import pprint

import requests

# url = 'http://5.63.153.31:5051/v1/account'
# headers = {
#     'accept': '*/*',
#     'Content-Type': 'application/json'
# }
# json = {
#     "login": "1o3ptest",
#     "email": "13optest@ru",
#     "password": "12345&"
# }
#
#
# response = requests.post(
#     url=url,
#     headers=headers,
#     json=json
# )
url = 'http://5.63.153.31:5051/v1/account/d7f606a3-5ed6-49ba-a6d7-5dc2f252f8c2'
headers = {
    'accept': 'text/plain'
}

response = requests.put(
    url=url,
    headers=headers,
)

print(response.status_code)
pprint.pprint(response.json())
response_json=response.json()
print(response_json['resource']['rating']['quantity'])