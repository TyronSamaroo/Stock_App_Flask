import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("IEX_TOKEN")

print(token)
from iexfinance.stocks import Stock
a = Stock("AAPL", token=token)
print(a.get_quote()['symbol'])
