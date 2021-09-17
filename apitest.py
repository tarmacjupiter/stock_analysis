import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

# Plot everything by leveraging the very powerful matplotlib package
# hist['Close'].plot(figsize=(16, 9))

msft = yf.Ticker("MSFT")

# Download stock data then export as CSV
data_df = yf.download("AAPL", start="2021-09-01", end="2021-09-08")
# data_df.to_csv('aapl_september.csv')

# get stock info
print(msft.info)

# get historical market data
hist = msft.history(period="5d")
