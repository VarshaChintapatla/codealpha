# Stock Portfolio Tracker

## Overview
The **Stock Portfolio Tracker** is a Python-based interactive application that allows users to manage their stock investments. Users can add, remove, and track the performance of their stock portfolio using real-time market data from Yahoo Finance (`yfinance`).

## Features
- 📊 **Add Stocks**: Users can add stocks to their portfolio by entering the stock symbol and quantity.
- ❌ **Remove Stocks**: Users can remove stocks from their portfolio.
- 📈 **View Performance**: Fetches historical stock prices and calculates portfolio value over time.
- 📉 **Graphical Visualization**: Displays a line chart of portfolio performance.

## Requirements
Ensure you have Python installed (version 3.x recommended) along with the following dependencies:

```bash
pip install yfinance pandas numpy plotly
```

## How to Use
1. Run the script:

   ```bash
   python stock_portfolio_tracker.py
   ```

2. Choose from the menu options:
   - `1` ➝ Add a stock to your portfolio.
   - `2` ➝ Remove a stock from your portfolio.
   - `3` ➝ View portfolio performance.
   - `4` ➝ Exit the program.

3. When viewing performance, the script fetches stock prices and displays a line chart.

## Example Usage
```
📈 Stock Portfolio Tracker 📉
1️⃣ Add Stock
2️⃣ Remove Stock
3️⃣ View Portfolio Performance
4️⃣ Exit
Enter your choice: 1
Enter stock symbol (e.g., AAPL, TSLA): AAPL
Enter quantity of AAPL: 10
✅ Added 10 shares of AAPL to the portfolio.
```

## License
This project is open-source and available under the MIT License.

