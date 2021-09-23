import sys  # Import system
from yahoo_fin import stock_info as si  # Used to find live value of stock
from csv import DictReader, reader  # Used to create CSV and read CSV
from decimal import *  # Used to convert percent String to decimal value

# Takes the total price invested in all the stocks in the Stock Portfolio
total_price = float(input("Total Price in portfolio: "))

# Create a new CSV file, given 'Write' privledges
sys.stdout = open("stocks-data.csv", "w")

# Header names for the CSV file
print("Company Name,Ticker,Current Stock Price,Percentage,Proposed")

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
        proposed = total_price * percent_quotient

        # Print all the data and save data to a file to read
        print(row["Name"] + "," + row["Ticker"] + "," +
              str(stock_live_price) + "," + row["Percent"] + "," + str(proposed))

sys.stdout.close()
