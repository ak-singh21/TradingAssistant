# Stock Trading Assistant

## What This Code Does

This Python script is a simple stock trading assistant. It downloads stock data, calculates two common technical indicators (Simple Moving Averages, or SMAs), and generates buy or sell signals based on these indicators. It then simulates trading with a starting amount of $10,000 and calculates the final portfolio value after backtesting the strategy.

## Features

- Fetches stock data from Yahoo Finance using `yfinance`.
- Calculates two types of SMAs (20-day and 50-day).
- Generates buy or sell signals based on when the 20-day SMA crosses the 50-day SMA.
- Simulates a basic trading strategy with $10,000 starting capital.
- Backtests the strategy and gives the final value of the portfolio after trades.
- Shows a graph with the stock prices, SMAs, and buy/sell signals using `matplotlib`.

## How It Works

1. **Get Stock Data**:  
   The script uses `yfinance` to fetch stock data from Yahoo Finance. You can change the stock ticker and date range to whatever you want. For example, it can get Apple stock data (AAPL) from January 1, 2020 to January 1, 2023.

2. **Calculate SMAs**:  
   It calculates the 20-day Simple Moving Average (SMA_20) and the 50-day Simple Moving Average (SMA_50). These are just average prices over a certain number of days and help to smooth out price fluctuations.

3. **Generate Buy/Sell Signals**:  
   The script creates buy and sell signals:
   - **Buy signal**: When the 20-day SMA crosses above the 50-day SMA.
   - **Sell signal**: When the 20-day SMA crosses below the 50-day SMA.

4. **Backtesting**:  
   It simulates trading. Starting with $10,000, the script buys as many shares as possible when there's a buy signal and sells them when there's a sell signal. It calculates the total value of your portfolio after all trades are completed.

5. **Plotting**:  
   It creates a graph showing the stock's closing price, the SMAs, and the buy and sell signals (green arrows for buys, red arrows for sells).

