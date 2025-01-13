# Import necessary libraries
import yfinance as yf  # For fetching stock data
import numpy as np      # For numerical operations
import pandas as pd     # For data manipulation
import matplotlib.pyplot as plt  # For plotting data

# Function to fetch historical stock data
def get_stock_data(ticker, start_date, end_date):
    # Download stock data from Yahoo Finance
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data  # Return the fetched data

# Example: Get Apple stock data from Jan 1, 2020 to Jan 1, 2023
data = get_stock_data('AAPL', '2020-01-01', '2023-01-01')
print(data.head())  # Print the first few rows of the data

# Function to add technical indicators to the stock data
def add_indicators(data):
    # Calculate the 20-day Simple Moving Average (SMA)
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    # Calculate the 50-day Simple Moving Average (SMA)
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    return data  # Return the updated data with indicators

# Add indicators to the data
data = add_indicators(data)
print(data[['Close', 'SMA_20', 'SMA_50']].tail())  # Print the last few rows of Close and SMA values

# Function to generate buy/sell signals based on moving averages
def generate_signals(data):
    data['Signal'] = 0  # Initialize the Signal column to 0
    # Create buy signals (1) when SMA_20 crosses above SMA_50, else 0
    data['Signal'] = np.where(data['SMA_20'] > data['SMA_50'], 1, 0)
    # Identify positions (1 for buy, -1 for sell)
    data['Position'] = data['Signal'].diff().fillna(0)  # Calculate the difference in signals
    return data  # Return the updated data with signals

# Generate buy/sell signals
data = generate_signals(data)
print(data[['Close', 'Signal', 'Position']].tail())  # Print the last few rows of Close, Signal, and Position

# Function to backtest the trading strategy
def backtest_strategy(data):
    initial_capital = 10000  # Set initial capital for trading
    shares = 0  # Initialize shares owned
    cash = initial_capital  # Start with the initial cash

    # Function to backtest the trading strategy
def backtest_strategy(data):
    initial_capital = 10000  # Set initial capital for trading
    shares = 0  # Initialize shares owned
    cash = initial_capital  # Start with the initial cash

    # Loop through each row of data using itertuples for efficiency
    for row in data.itertuples(index=False, name=None):  # Use tuples instead of named tuples
        position = row[6]  # Access the 'Position' column (adjust index based on your DataFrame)
        close_price = row[0]  # Access the 'Close' column (adjust index based on your DataFrame)

        if position == 1.0:  # Buy signal
            shares = cash // close_price  # Buy as many shares as possible
            cash -= shares * close_price  # Deduct the cost from cash
        elif position == -1.0:  # Sell signal
            cash += shares * close_price  # Sell all shares and add to cash
            shares = 0  # Reset shares to zero after selling

    # Calculate total portfolio value at the end of the period
    total_value = cash + shares * data['Close'].iloc[-1]
    return total_value.item()  # Return as a scalar value (use .item() to convert Series to scalar)

# Backtest the strategy and get the final portfolio value
final_value = backtest_strategy(data)
print(f"Final portfolio value: ${final_value:.2f}")  # Print the final portfolio value

# Function to plot stock price and buy/sell signals
def plot_signals(data):
    plt.figure(figsize=(12, 6))  # Set the figure size
    plt.plot(data['Close'], label='Close Price', alpha=0.5)  # Plot the closing price
    plt.plot(data['SMA_20'], label='SMA 20', alpha=0.75)  # Plot the 20-day SMA
    plt.plot(data['SMA_50'], label='SMA 50', alpha=0.75)  # Plot the 50-day SMA

    # Plot buy signals with green arrows
    plt.plot(data[data['Position'] == 1].index, 
             data['SMA_20'][data['Position'] == 1], 
             '^', markersize=10, color='g', lw=0, label='Buy Signal')

    # Plot sell signals with red arrows
    plt.plot(data[data['Position'] == -1].index, 
             data['SMA_20'][data['Position'] == -1], 
             'v', markersize=10, color='r', lw=0, label='Sell Signal')

    plt.title('Stock Price with Buy and Sell Signals')  # Set the title of the plot
    plt.legend()  # Show the legend
    plt.show()  # Display the plot

# Call the function to plot the signals
plot_signals(data)
