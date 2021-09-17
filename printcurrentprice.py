import yfinance as yf
from yahoo_fin import stock_info as si


# Ask for which stock the user would like to see the current price for
stock = input(
    "Which stock would you want me to retrieve the live price for?: ")

# Print out the current market price of the stock, rounds to the hundredth's place
print(round(si.get_live_price(stock), 2))
