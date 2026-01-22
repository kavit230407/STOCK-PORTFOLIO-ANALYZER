from decimal import Decimal
def cal_daily_returns(prices):
    if type(prices)!=list or len(prices)<2:
        print('THERE IS SOMETHING WRONG PLS CHECK!')
        return []
    if any(p<0 for p in prices):
        print('all prices must be positive!')
        return []

    returns=[]
    prices_dec=[Decimal(str(p)) for p in prices]
    for i in range(1, len(prices_dec)):
        daily_return=(prices_dec[i]-prices_dec[i-1])/prices_dec[i-1]
        returns.append(daily_return)
    return returns

def cal_total_returns(prices):
    if type(prices)!=list or len(prices)<2:
        print('THERE IS SOMETHING WRONG PLS CHECK !')
        return Decimal('0')
    if any(p<0 for p in prices):
        print('all prices must be positive!')
        return Decimal('0')
    
    
    prices_dec=[Decimal(str(p))for p in prices]
    return (prices_dec[-1]-prices_dec[0])/prices_dec[0]

def risk_indicator(prices):
    returns=cal_daily_returns(prices)
    if not returns:
        return 'INSUFFICIENT DATA'
    for r in returns:
        if r< Decimal('-0.30'):
            return 'HIGH VOLATILITY'
    return 'LOW VOLATILITY'

def best_worst_stock(total_returns):
    if not total_returns:
        print('there are no stocks provided')
        return 'N/A'
    else:
     return f' best return {max(total_returns.values())*100:0.2f}%\n worst return {min(total_returns.values())*100:0.2f}%'

print(best_worst_stock({'stock A': cal_total_returns([100, 102, 101, 104, 103, 105]), 'stock B': cal_total_returns([50, 52, 51, 53, 54, 55]), 'stock C':cal_total_returns([200, 198, 205, 210, 208, 212])}))       

def cal_portfolio_return(total_returns,weights):
    if len(total_returns)!=len(weights):
        print('there is something wrong pls check !')
        return Decimal('0')
    if abs(sum(weights)-1)>0.001:
        print('warning! weights do not sum 1 so results may be incorrect')
        
    
    portfolio_return=Decimal('0')
    for stocks,weight in zip(total_returns.values(),weights):
          portfolio_return+=stocks*Decimal(str(weight))
    return  portfolio_return

def investment_analysis(total_returns,weights):
    investment_return=cal_portfolio_return(total_returns,weights)
    if investment_return<0.15:
        return f' HOLD: NO FURTHER CAPITAL ADDITION' 
    return f'INVEST MORE: PORTFOLIO IS PERFORMING WELL'

total_returns = {
    'Stock A': cal_total_returns([100, 102, 101, 104, 103, 105]),
    'Stock B': cal_total_returns([50, 52, 51, 53, 54, 55]),
    'Stock C': cal_total_returns([200, 198, 205, 210, 208, 212])
}

weights = [0.4, 0.3, 0.3]

portfolio_return = cal_portfolio_return(total_returns, weights)
print(f'portfolio return:{float(portfolio_return*100):0.2f}%')
print(investment_analysis(total_returns, weights))





