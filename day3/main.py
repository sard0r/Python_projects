import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api = '3ac1ec481a314581ac157b54d52b8fc9'

params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": "NXWRDS1B5L7X9RLC"
}

news_params = {
    "q": "tesla",
    "from": "2023-03-31",
    "sortBy": "publishedAt",
    "apiKey": "3ac1ec481a314581ac157b54d52b8fc9"
}

response = requests.get(STOCK_ENDPOINT, params=params)
data = response.json()
Today = float(data['Time Series (60min)']['2023-03-31 20:00:00']['4. close'])
Yesterday = float( data['Time Series (60min)']['2023-03-30 20:00:00']['4. close'])

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(Today-Yesterday)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = (Yesterday*100)/Today
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()['articles']
    news_array = [news_data[i] for i in range(3)]
    formatted_articles = [f"Headline:{article['title']}. \nBrief:{article['description']}" for article in news_array]
    print(formatted_articles)
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC554d56090fa74d103dd5710cc4fcdf47"
auth_token = "074c31dafece1f9b574534fc878a3d71"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Ziyod aka bilaman siz meni endi kechirmaysiz. Uzur roza kunida meni kechiring barcha bolgan ishlar uchun. Chiroyli hayot qurib yashang iltimos.",
  from_="+15856591868",
  to="+998900661901"
)
print(message.sid)