import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "3DTVXRGP7951VIZT"
STOCK_FUNCTION = "TIME_SERIES_DAILY"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "f9ac8e903cd542bbbd0d61f45a94f09f"


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    'function': STOCK_FUNCTION,
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

# if difference > 0:
#     DIRECTION = "🔺"
# else:
#     DIRECTION = "🔻"
# positive = abs(difference)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(day_before_yesterday_closing_price)) * 100

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diff_percent > 0:
    news_params = {
        'q': COMPANY_NAME,
        'from': yesterday_data,
        'sortBy': 'popularity',
        'apiKey': NEWS_API
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']

# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.
#
# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
# headline = [article['title'] for article in stock_news[0]]
# description = [article['description'] for article in stock_news[0]]
#
# TODO 9. - Send each article as a separate message via Twilio.
# print(f'{STOCK_NAME}: {DIRECTION}{percentage}%\nHeadline: {headline[0]}\nBrief: {description[0]}')
#
#
# Optional TODO: Format the message like this:

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

