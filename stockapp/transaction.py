import os
from dotenv import load_dotenv
from iexfinance.stocks import Stock
load_dotenv()


token = os.getenv("IEX_TOKEN")


from iexfinance.stocks import Stock
tsla = Stock('TSLA')
print(tsla.get_price())