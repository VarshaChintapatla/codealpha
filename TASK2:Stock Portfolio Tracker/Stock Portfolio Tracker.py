import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}  # Dictionary to hold stock symbols and their quantities

    def add_stock(self, symbol, quantity):
        """Add a stock to the portfolio."""
        symbol = symbol.upper()  # Ensure stock symbols are uppercase
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"✅ Added {quantity} shares of {symbol} to the portfolio.")

    def remove_stock(self, symbol, quantity):
        """Remove a stock from the portfolio."""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= quantity:
                self.portfolio[symbol] -= quantity
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]
                print(f"✅ Removed {quantity} shares of {symbol}.")
            else:
                print(f"❌ Cannot remove {quantity} shares of {symbol}. Only {self.portfolio[symbol]} available.")
        else:
            print(f"❌ {symbol} is not in the portfolio.")

    def fetch_data(self):
        """Fetch historical data for the stocks in the portfolio."""
        if not self.portfolio:
            print("❌ No stocks in the portfolio.")
            return None
        symbols = list(self.portfolio.keys())
        data = yf.download(symbols, period='1mo')['Close']
        return data

    def calculate_portfolio_value(self, data):
        """Calculate the total value of the portfolio."""
        if data is None:
            return None
        portfolio_value = (data * pd.Series(self.portfolio)).sum(axis=1)
        return portfolio_value

    def plot_portfolio_performance(self, portfolio_value):
        """Plot the performance of the portfolio."""
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=portfolio_value.index, y=portfolio_value, mode='lines', name='Portfolio Value'))
        fig.update_layout(title='Portfolio Performance Over Time',
                          xaxis_title='Date',
                          yaxis_title='Value (USD)')
        fig.show()


# 🚀 Interactive Stock Portfolio Tracker (Runs Immediately)
tracker = StockPortfolioTracker()

while True:
    print("\n📈 Stock Portfolio Tracker 📉")
    print("1️⃣ Add Stock")
    print("2️⃣ Remove Stock")
    print("3️⃣ View Portfolio Performance")
    print("4️⃣ Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").strip().upper()
        quantity = int(input(f"Enter quantity of {symbol}: "))
        tracker.add_stock(symbol, quantity)

    elif choice == '2':
        symbol = input("Enter stock symbol to remove: ").strip().upper()
        quantity = int(input(f"Enter quantity to remove: "))
        tracker.remove_stock(symbol, quantity)

    elif choice == '3':
        data = tracker.fetch_data()
        if data is not None:
            portfolio_value = tracker.calculate_portfolio_value(data)
            print(portfolio_value)
            tracker.plot_portfolio_performance(portfolio_value)

    elif choice == '4':
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter a number between 1-4.")
