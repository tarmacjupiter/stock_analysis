import yfinance as yf
from yahoo_fin import stock_info as si
from csv import reader

# skip over the header of the cvs file
with open('nyse-listed_csv.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check if the file is empty
    if header != None:
        # Iterate over each row after the header in the cvs
        for row in csv_reader:
            # row variable is a list that represents a row in cvs
            print(row[0])


# # Ask for which stock the user would like to see the current price for
# stock = input(
#     "Which stock would you want me to retrieve the live price for?: ")

# Print the stock name from the abbreviation
# (yfinance)
# stock_abrev = yf.Ticker(stock)

# company_name = stock_abrev.info['longName']

# # Print out the current market price of the stock, rounds to the hundredth's place
# # (yahoo_fin)
# print(company_name + ":")
# print(round(si.get_live_price(stock), 2))
