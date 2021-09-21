# stock_project

1. Have an assistant load the $ in the current column from client statements.

2. Have the program reach out to get the current price of each listed holding from the internet. I currently use FINVIZ.com to key in the ticker symbol but any source would be fine i.e., Yahoo finance etc.

3. Have the percentage of weighting calculate the shares to buy/sell.

---

> modelworksheet.csv

**is the original file**

---

> stocks.csv

**is the new file where the new data table with current prices are created**

`sys.stdout = open("stocks.csv", "w")`

_made from ^^^ command_

---

# FROM THE CALL

19% (sugggested amount)

23% (current percentage)

4% difference

---

99.99

100,000

19,000 | 19% = lower (could be higher)

24,000 | 24% = higher (could be lower)

    	(Use negative interger)

higher - lower = 5,000 (call it difference)

difference / current_stock = (amount to sell) 50

---

when going from lower percentage to higher = sell

when going from higher percentage to lower = buy

---

(round to the lower share)

if current stock difference percentage is lower than the current live
price of the stock, do not buy OR sell the stock

---

100,000 \* .02 = 2000 / 118.82 = 16

(proposed is the percentage times the total stock amount) (300,000 \* .19)

(current live stock price \* number of shares)

---

use current and proposed

proposed > current ---> buy

current > proposed ----> sell

---

current is total times the percentage divided by amount of the live share stock price

current is the market value from the statement that the assistant keys in
(total dollar amount of statement) (no computation)
proposed 57,000
current 55,000
got the number from the statement

proposed is the percentage times the total account value

(no computation in column C or D)

(put the buys and the sells in a word file)
