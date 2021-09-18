# stock_project

1. Have an assistant load the $ in the current column from client statements.

2. Have the program reach out to get the current price of each listed holding from the internet. I currently use FINVIZ.com to key in the ticker symbol but any source would be fine i.e., Yahoo finance etc.

3. Have the percentage of weighting calculate the shares to buy/sell.

---

> modelworksheet.csv

**is the original file**

> stocks.csv

**is the new file where**

`sys.stdout = open("stocks.csv", "w")`

**was created**
