import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "sardor97"
TOKEN = "Sardor5822613Sj$"
GRAPH_ID = "graph1"

# user_params = {
#     "token": "Sardor5822613Sj$",
#     "username": "sardor97",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }




# response = requests.post(url=pixela_endpoint, json = user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit":"hours",
    "type": "float",
    "color": "ajisai"
}



headers ={
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json = graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": "20230404",
    "quantity":"3",
}

year = "20230404"
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update 

response = requests.put(url=pixel_creation_endpoint, json=year)
print(response.text)