import sys  # Import system
import math # Self-explanatory 
from yahoo_fin import stock_info as si  # Used to find live value of stock
from csv import DictReader, reader  # Used to create CSV and read CSV
from decimal import *  # Used to convert percent String to decimal value

# Takes the total price invested in all the stocks in the Stock Portfolio
total_price = float(input("Total Price in portfolio: ")) 

print(total_price)

# Create a new CSV file, given 'Write' privledges
sys.stdout = open("Stock-Data/stocks-data.csv", "w")

# Header names for the CSV file
print("Company Name,Ticker,Current Stock Price,Percentage,Proposed,Current,Buys,Sells")

# skip over the header of the cvs file
with open('modelworksheet.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    # Check if the file is empty
    # Iterate over each row after the header in the cvs
    for row in csv_dict_reader:
        # row variable is a list that represents a row in cvs

        # # Save the current market price of the stock, rounds to the hundredth's place
        # # (yahoo_fin)
        stock_live_price = round(si.get_live_price(row["Ticker"]), 2)

        # Get percentage
        percentage = row["Percent"]

        # Remove annoying "%" symbol
        remove_perc_sign = percentage.replace("%", "")

        # Convert percentage String to an int
        # USE IF NEED TO COMPARE PERCENT DEMICAL VALUE
        percent_int = float(remove_perc_sign)

        # Divide percent_int by 100
        percent_quotient = percent_int / 100.00

        # Proposed column
        proposed = round(total_price * percent_quotient, 2)

        #Buys or Sells

        #Converts row["Current"] index to a float variable
        current_to_str = float(row["Current"])

        #Gets the raw data for proposed - current
        buys_or_sells = proposed - current_to_str

        #Divides the buys_or_sells by the current live stock price for that index
        buys_sells = buys_or_sells / stock_live_price

        #Initialization of Buys and Sells
        buys = 0
        sells = 0

        #Logic to calculate what to buy or sell
        if(buys_sells > 0):
            buys = buys_sells
            sells = 0
        elif(buys_sells < 0):
            buys = 0
            sells = abs(buys_sells)
        elif(abs(buys_or_sells) < stock_live_price):
            buys = 0
            sells = 0
        else:
            buys = 0
            sells = 0

        # Print all the data and save data to a file to read
        print(row["Name"] + "," + row["Ticker"] + "," +
              str(stock_live_price) + "," + row["Percent"] + "," + str(proposed) + "," + row["Current"] + "," + str(math.floor(buys)) + "," + str(math.floor(sells)))

sys.stdout.close()
