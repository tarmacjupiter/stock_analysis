import sys  # Import system
import yfinance as yf  # Get long name from Ticker (may not need to be used)
from yahoo_fin import stock_info as si  # Used to find live value of stock
from csv import DictReader, reader  # Used to create CSV and read CSV
from decimal import *  # Used to convert percent String to decimal value

# Create a new CSV file, given "Write" privledges
sys.stdout = open("stocks.csv", "w")

print("Company Name,Ticker,Current Stock Price,Percentage")

# skip over the header of the cvs file
with open('modelworksheet.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    # Check if the file is empty
    # Iterate over each row after the header in the cvs
    for row in csv_dict_reader:
        # row variable is a list that represents a row in cvs

        # Save yfinance.Ticker object ACT symbol in stock_abrev
        # stock_abrev = yf.Ticker(row["Ticker"])

        # Logic for getting extended name of ACT symbol, not fully functional
        # company_name = stock_abrev.info['longName']

        # # Save the current market price of the stock, rounds to the hundredth's place
        # # (yahoo_fin)
        stock_live_price = round(si.get_live_price(row["Ticker"]), 2)

        # Get percentage
        percentage = row["Percent"]
        # Remove annoying "%" symbol
        remove_perc_sign = percentage.replace("%", "")
        # Convert percentage String to an int
        # USE IF NEED TO COMPARE PERCENT DEMICAL VALUE
        percent_int = Decimal(remove_perc_sign)

        # Print all the data and save data to a file to read
        print(row["Name"] + "," + row["Ticker"] + "," +
              str(stock_live_price) + "," + row["Percent"])

sys.stdout.close()
