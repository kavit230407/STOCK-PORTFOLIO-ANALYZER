import pandas as pd
import yfinance as yf
from datetime import datetime,timedelta
def analysis_of_stock(symbol):
    try:
        end=datetime.today()
        start=end-timedelta(days=60)
        df=yf.download(symbol,start=start,end=end,progress=False)
        if df.empty:
            return 'no data can be fetched'
        if isinstance(df.columns,pd.MultiIndex):
            df.columns=df.columns.get_level_values(0)
        close='Close' if 'Close' in df.columns else "Adj Close"
        open='Open'
        df['daily return']=df[close].pct_change().fillna(0).round(2)*100
        df['intraday return']=((df[close]-df[open])/df[open]*100).round(2)

    except Exception as e:
        return f' there is something wrong! {e}'
    return df


def volatility_analysis(df):
    volatile_day=df[df['intraday return']<-0.3]
    non_volatile_days=df[df['intraday return']>-0.3]
    if len(volatile_day)>=len(non_volatile_days):
        return f' volatile days:{(len(volatile_day)/len(df))*100:.2f}%\nnon volatile days{(len(non_volatile_days)/len(df))*100:.2f}%\nVOLATILITY STATUS: HIGH VOLATILITY'
    else:
        return f'volatile days:{(len(volatile_day)/len(df)*100):.2f}%\nnon volatile days:{(len(non_volatile_days)/len(df))*100:.2f}%\nVOLATILITY STATUS: LOW VOLATILITY'
       
def monthly_returns(df):
    monthly_close=df['Close'].resample('ME').last()
    monthly_return=monthly_close.pct_change().dropna().round(2)*100
    return f'monthly return\n{monthly_return.to_string()}'

def performance_analysis(total_return):
    if total_return<-3:
        return 'WEAK'
    elif 0<total_return<1:
        return 'DECENT'
    else:
        return 'GOOD'
    
def investment_guide(performance):
    if performance=='WEAK':
        return 'SELL AND RECOVER INVESTMENT'
    elif performance=='DECENT':
        return 'HOLD THE STOCK'    
    else:
        return 'GOOD TIME FOR INVESTING'
    

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
          

 

    




    