from twilio.rest import Client

class NotificationManager:
    
    def send_notification(searchprice, originalprice, departurecity, Departure_Airport_code, Arrival_City_Name, Arrival_Airport_code, Outbound_Date, Inbound_Date):
        if searchprice < originalprice:
            #This class is responsible for sending notifications with the deal flight details.   
            # Set environment variables for your credentials
            # Read more at http://twil.io/secure
            account_sid = "AC554d56090fa74d103dd5710cc4fcdf47"
            auth_token = "3fe813d933749896f316a5f87ba0ffb8"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            body=f"Low price alert!, Only {searchprice}$ to fly from {departurecity}-{Departure_Airport_code} to {Arrival_City_Name}-{Arrival_Airport_code}, from {Inbound_Date} to {Outbound_Date}",
            from_="+15856591868",
            to="+821073489707"
            )
    