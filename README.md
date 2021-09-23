# Stock Analysis

---

## Stock Analysis for Windows 10

1. Press the Green (&#x1F4D7;) "Code" button

2. Download the files by pressing "Download Zip"

3. Extract the files anywhere on your computer
   ⋅⋅\* (Extract the files in a location where you will have easy access)

4. Go into the "Installation Folder"

5. Right click "install-requirements.ps1"

6. Press, "Run with PowerShell"
   ⋅⋅\* (The PowerShell program will automatically close once it has installed all dependencies)

7. Head back into the main folder directory

8. Right click "run_script.ps1"

9. Press "Run with PowerShell"

10. After the program is done processing the new data will be stored in "stocks-data.csv"

---

## Stock Analysis for MacOS and Linux

1. Open terminal in the Stock Analysis directory location

2. cd into Installation folder

3. Then type

```console
$ pip install -r requirements.txt

```

4. Then go into main directory folder

5. Then type in the shell

```console
python stock.py
```

⋅⋅\* (May need to type "python3 stock.py" depending on installtion and build of Python)

---

### For Developers

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
