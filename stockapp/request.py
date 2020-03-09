import os
from dotenv import load_dotenv
import requests
load_dotenv()

from collections import namedtuple

Stock = namedtuple('Stock','price, close')
token = os.getenv("API_KEY")
ticker = 'MSFT'

def stock_info(ticker):
    """[Returns Info on the stock as a namedtuple where you can access price and closing value]
    
    Arguments:
        ticker {[string]} -- [The ticker symbol of a stock]
    
    Returns:
        [namedtuple] -- [return Stock Object with acess to price of stock and closing value of stock]
    """
    
    URL = "https://www.alphavantage.co/query?"
    PARAMS = {'function' : 'GLOBAL_QUOTE',
          'symbol': ticker,
          'apikey': token}
    r = requests.get(url = URL, params= PARAMS)

    data = r.json()
    return Stock(price = data["Global Quote"]["05. price"], 
                   close = data["Global Quote"]["02. open"])

def is_valid_ticker(ticker):
    URL = "https://www.alphavantage.co/query?"
    PARAMS = {'function' : 'GLOBAL_QUOTE',
          'symbol': ticker,
          'apikey': token}
    

    