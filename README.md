# FINE3300-2026-A2

### Description
- FINE 3300, Fall 2026, Assignment 2
- I made an inflation calculator and a CPI graph in Python, based on the [Bank of Canada Inflation Calculator](https://www.bankofcanada.ca/rates/related/inflation-calculator/).
- The Bank of Canada calculator only lets you pick a year. I've enhanced it so you can pick a month and a year.

### Files
- `Inflation_Calc.py` - asks for a price and two dates, prints the results, then shows the CPI graph and saves it as `CPI_Graph.png`
- `STATIC_INFLATIONCALC.csv` - the CPI data from the Bank of Canada
- `CPI_Graph.png` - the graph of the CPI and the annual % change

### How to use it
1. Install pandas and matplotlib if you don't have them:
   ```
   pip install pandas matplotlib
   ```
2. Download all the files and put them in the same folder.
3. Open that folder in VS Code (File → Open Folder).
4. Run `Inflation_Calc.py`. It will ask you for:
   - the price (just the number, e.g. `1000`). Any number except 0 works, including negatives (same as the BoC website).
   - the first date (e.g. `1995-07`)
   - the second date (e.g. `2026-09`)
5. It prints the results, then shows the CPI graph.

If you type something wrong, it tells you and asks again.

Example:
```
Enter the price: abc
Invalid price. Enter a number, e.g. 100 or 100.50
Enter the price: 1000
Enter the first date (YYYY-MM): 1800-01
Invalid date. Use YYYY-MM between 1914-01 and 2026-09
Enter the first date (YYYY-MM): 1995-07
Enter the second date (YYYY-MM): 2026-09
```

### Sample Output
```
--------------------------------------------------
$1,000.00 CAD in 1995-07 would cost $1,934.02 CAD in 2026-09
Percent change: 93.40%
Number of years: 31.17
Average annual rate of inflation: 2.14%
CPI for 1995-07: 87.9
CPI for 2026-09: 170.0
2002 CPI = 100.0
--------------------------------------------------
```

### CPI Graph

![CPI Graph](CPI_Graph.png)

**Commentary:**

The CPI (blue line) stays low and flat until around 1970, then rises quicker faster. The dotted line is the base level of 100, which the CPI reaches in 2002.

Some interesting parts of the annual % change (orange line):
- During and after WWI (about 1917–1920), inflation spiked to over 20%. Then prices dropped sharply in 1921, to about -18%.
- In the early 1930s (Great Depression), prices went down again, so the line goes below 0%.
- Right after WWII, around 1948, inflation jumped to about 17%.
- In the 1970s and early 1980s, inflation was really high, over 10% at times.
- Since the early 1990s, inflation has mostly stayed around 2%, which is the Bank of Canada's target.
- In 2022, after COVID, inflation jumped to around 8%, the highest in about 40 years.

### Data Source
Bank of Canada: https://www.bankofcanada.ca/valet/observations/STATIC_INFLATIONCALC/csv
