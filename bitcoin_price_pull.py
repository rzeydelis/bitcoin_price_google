# Import the libraries
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
import pandas as pd


# Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):
    # Get the URL
    url = "https://www.google.com/search?q=" + coin + "+price"

    # Make a request to the website
    HTML = requests.get(url)

    # Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')

    # Find the current price
    # text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    text = soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find("div",
                                                                         attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    # Return the text
    return text


# Create a main function to consistently show the price of the cryptocurrency
def tracker():
    # Create an infinite loop to continuously show the price
    price = ()
    while True:
        # Choose the cryptocurrency that you want to get the price of (e.g. bitcoin, litecoin)
        crypto = 'bitcoin'

        # get current datetime
        created_at = datetime.now()
        # Get the price of the crypto currency and format it as a float
        price = get_crypto_price(crypto)
        price = float(price.replace(' United States Dollar', '').replace(',', ''))

        # print price
        print(price)
            
        time.sleep(300)
