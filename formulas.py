# Useful functions
import numpy as np

def sharpe(returns): # Sharpe ratio
    m=np.mean(returns)
    s=np.std(returns)
    return float(m)/s

def autocorr(x):
    result = np.correlate(x, x, mode='full')
    maxcorr = np.argmax(result)
    #print 'maximum = ', result[maxcorr]
    result = result / result[maxcorr]
    return result[result.size/2:]

def HPR(X, f):
    return 1 + f * (- X / min(X))
    
def TWR(X, f):
# Terminal Wealth Return z wektora X dla zadanego f
    return np.prod(HPR(X, f))

def f(X):
    f = 0.00
    k = 0.01
    while ( TWR(X, f) < TWR(X, f + k) ):
        if f > 1.0:
            break
        f = f + k
#if f -- 0 or f > 1 raise exception
    return f
    
def gvsf(X): # G vs. f (or GAT vs f or TWR vs f)
    n = len(X)
    # m = min(X)
    Y = []
    for i in xrange(100):
        fi = float(0.01*i)
        G = TWR(X,fi) ** (1.0/n) - 1 # < 0 oznacza straty
        #GAT = G * (- m/fi);
        Y = Y + [[fi, G]]
    return np.array(Y)
    
def ror2dolar(ror, position_size = 1.0, holding_period = 3.0, buy=3.00, coc = 0.03, commission_per_lot=50.0):
#all is well with RoR but how much in dollars do you really make? what is your cost of carry? etc.
#This is all just estimation and rule of thumb nothing set in stone
    lever = 1.0/100     # such is your broker's margin requirement
    lot_size = 100000.0 # you buy and sell 100 000 USD
    # coc [differential of cost of money between currencies] = 3% in anual terms but of the entire lot
    sell = (1+ror)*buy  # logicaly this is your selling price 
    dolar_return = (sell-buy)*lot_size*lever #'dollar' it is not. It's home currency actually
    cost_of_carry = (sell+buy)/2 * (coc/365 * holding_period)*lot_size #average by buy/sell price
    comission = commission_per_lot * position_size            # fixed commision and spread estimated per lot
    net_dollar_profit = dolar_return - cost_of_carry - comission
    return net_dollar_profit, dolar_return, cost_of_carry, comission
    
def clean_signal(signals, horizon): #Only first instance of signal is taken, so clean following
    x = signals[0]
    temp = [x]
    for i in range(len(signals)):
        if signals[i] > x + horizon:
            temp = temp + [signals[i]]
            x = signals[i]
    return np.array(temp)

def sell(signals, horizon, max_length): # Simple time exits 
    temp = signals + horizon
    for i in xrange(len(temp)):    
        if temp[i] >= max_length:
            temp[i] = max_length-1 #Maximum index cannot extend beyond range of close[]
    return temp