# STOCK & PORTFOLIO ANALYZER

A Python project for stock market analysis using real-time data from Yahoo Finance (yfinance) and pandas.

This repo contains **two separate tools**:

1. **Portfolio Return Calculator** — Multi-stock portfolio analysis with weighting  
2. **Stock Analysis Tool** — Deep single-stock analysis with returns, volatility, monthly trends, and basic advice

## Features

### Portfolio Return Calculator
- Fetches live historical data for multiple stocks (Reliance, HDFC Bank, TCS)
- Calculates:
  - Daily returns
  - Total returns
  - Portfolio return (weighted average)
  - Volatility status

### Stock Analysis Tool
- Analyzes any single stock symbol
- Calculates:
  - Daily & intraday returns
  - Best and Worst day Based on intraday return
  - Precise percentage of no of days being volatile and non volatile
  - Volatility classification (high/low)
  - Monthly returns (based on last closing price)
  - Performance rating (WEAK / DECENT / GOOD)
  - Basic investment advice

## Technologies Used
- Python 3
- yfinance — real-time stock data fetch
- pandas — data manipulation & analysis
- 
# HOW TO RUN PORTFOLIO RETURN CALCULATOR

reliance = get_prices('RELIANCE.NS')
hdfc = get_prices('HDFCBANK.NS')
tcs = get_prices('TCS.NS')

prices = {'RELIANCE': reliance, 'HDFC': hdfc, 'TCS': tcs}

# Total returns (once)
total_returns = cal_total_returns(prices)

# Portfolio
portfolio_return = cal_portfolio_ret(total_returns, [0.4, 0.3, 0.3])

# Daily returns
daily_returns = cal_daily_returns(prices)

# Print everything nicely

print(f"Portfolio Return: {float(portfolio_return * 100):.3f}%")
print(investment_analysis(total_returns, [0.4, 0.3, 0.3]))
print(best_worst_stock(total_returns))
print(risk_indicator(daily_returns))  # fix this function first

print('start date: 11/1/2026   end date: 21/01/2026')

# HOW TO RUN STOCK ANALYSIS TOOL

df=analysis_of_stock('RELIANCE.NS')
print(f'ANALYSIS OF STOCK: RELIANCE.NS\nFROM:{df.first_valid_index()} TO:{df.last_valid_index()}')
print(f'AVG DAILY RETURN:{df['daily return'].mean()*100:0.2f}%\nAVG INTRADAY RETURN:{df['intraday return'].mean()*100:.2f}%')

print(f'MAX PRICE:{df['Close'].max():.2f}\nMIN PRICE:{df['Close'].min():.2f}')

print(f'BEST DAY:{df['intraday return'].idxmax()}:{df['intraday return'].max()}%\nWORST DAY:{df['intraday return'].idxmin()}:{df['intraday return'].min()}%')

close='Close'if 'Close' in df.columns else 'Adj Close'

total_return=round(((df[close].iat[-1]/df[close].iat[0])-1)*100,2)

print(f'total return:{total_return}%')

print(volatility_analysis(df))

print(monthly_returns(df))

print(f'PERFORMANCE:{performance_analysis(total_return)}')

performance=performance_analysis(total_return)

print(f'ADVICE:{investment_guide(performance)}')

# JOURNEY
"Started with my own idea and code, wrote 60–80 lines per session myself. Got stuck on some bugs & polish points — Grok helped me fix them, make it more robust, and write cleaner pandas code.
"Used Grok (xAI) as a coding assistant for debugging and polish — similar to how developers use GitHub Copilot or Claude today.

# PORTFOLIO RETURN CALCULATOR OUTPUT

<img width="959" height="767" alt="screenshot (2)" src="https://github.com/user-attachments/assets/97da5831-28f4-4a69-ae12-072f99677dcd" />

# STOCK ANALYSIS TOOL OUTPUT

<img width="855" height="910" alt="screenshot2" src="https://github.com/user-attachments/assets/cf10e788-9b0d-4508-bf6d-472fa25b5272" />
