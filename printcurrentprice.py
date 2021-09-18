import yfinance as yf
from yahoo_fin import stock_info as si
from csv import DictReader, reader

# skip over the header of the cvs file
with open('modelworksheet.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    # Check if the file is empty
    # Iterate over each row after the header in the cvs
    for row in csv_dict_reader:
        # row variable is a list that represents a row in cvs

        stock_abrev = yf.Ticker(row["Ticker"])

        # Logic for getting extended name of ACT symbol, not fully functional
        company_name = stock_abrev.info['longName']

        print(company_name + ":")

        # # Print out the current market price of the stock, rounds to the hundredth's place
        # # (yahoo_fin)
        print(round(si.get_live_price(row["Ticker"]), 2))
        print("")


print("All done!")
