# Portfolio Return Calculator

A basic Python tool I built to calculate daily/total stock returns, portfolio weighted return, and a simple risk indicator.
# STOCK ANALYSIS TOOL
a basic tool that gives you the analysis of the given stock of last 60 days 


### Features Portfolio return Calculator
- Precise calculations using `decimal.Decimal` (no float rounding errors)
- Input validation (list type, length ≥2, positive prices)
- Weighted portfolio return with length & sum checks
- Basic risk flag (high volatility if any day < -30%)
- Safe error handling with messages
- using yfinance real world data

# Features of Stock Analysis Tool
-Calculation of Avegrage Daily return
-Calculation of Average Intraday return
-Precise Percentage of Volatile and Non Volatile Days
-Assesment of Volatilty Status Based on Percentage Of Volatile and Non Volatile days
-Max and Min price of Last 60 Days
-Best and Worst Day Based on Intraday return
-Monthly returns
-Total return
-Performance Analysis Based on Total return
-Basic Advice Based on Performance
 
### How to Run Portfolio Return Calculator
```python
# Fetch
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

### HOW TO RUN STOCK ANALYSIS TOOL
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

### What I Learned

Why float is dangerous for money → switched to Decimal
Importance of input validation to prevent crashes/wrong results
Iterative improvement based on feedback by grok made the core myself taken help to polish my project
 How to run your opreations faster using pandas
How to integrate yfinance and pandas for better result
How to use iat in built method of python so that we could get numeric total return instead of series 

Built with
Python (Udemy Complete Python Bootcamp by Jose Portilla – certificate earned)
### Example Output
![Project Output](screenshot.png)
<img width="959" height="767" alt="screenshot (2)" src="https://github.com/user-attachments/assets/ea0013b2-7b21-4b31-bf58-e75f92083f91" />
![Project Output](screenshot2.png)

<img width="855" height="910" alt="Screenshot 2026-02-16 143340" src="https://github.com/user-attachments/assets/7947422b-6684-44a5-b816-ff5a2ab2d282" />

