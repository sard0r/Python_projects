import requests

sheet_endpoint = "https://api.sheety.co/4526d01b0794b3df8b6e4cac1b5e0c4f/copyOfFlightDeals/users"

print("Welcome to the Sardor's Flight Club.")
print("We Find the best flight deals and email you")


# sheet_response = requests.get(url = sheet_endpoint)
# print(sheet_response.text)

UserFirstName= input("What is your First name?\n")
UserLastName= input("What is your Last name?\n")
UserEmail= input("What is your email address?\n")
UserEmailConfirm= input("Type your email again.\n")

if UserEmail == UserEmailConfirm:

    sheet_inputs = {
        "user":{
        "firstName": UserFirstName,
        "lastName": UserLastName,
        "email": UserEmail
    }}

    sheet_response = requests.post(url = sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)
