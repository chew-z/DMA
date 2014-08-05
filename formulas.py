# Useful functions
import numpy as np
import talib as talib

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
    
def f_lookbackdays(close, EMA = 60, min_l = 5, max_l = 20):
    deltaVol = np.zeros(len(close))
    stdev = talib.STDDEV(close, EMA)  
    z = zip(stdev[1:], stdev)
    i = 1
    for y, x in z:
        deltaVol[i] = np.log(y/x)
        i += 1
    del x, y, z, i
    
    deltaVol = np.nan_to_num(deltaVol)
    
    index_min = (deltaVol < -0.027)
    index_max = (deltaVol >  0.027)

    f_l = int(0.5 *(max_l - min_l)) * np.ones(len(deltaVol))
    f_l[index_min] = min_l
    f_l[index_max] = max_l
    return f_l
    
def f_hh_ll(f_l, high, low):
    hh = np.zeros(len(high))
    ll = np.zeros(len(low))
    
    m = max(f_l)
    for i in xrange(len(f_l)):
        l = f_l[i]
        if (i >= m):
            hh[i] = max(high[i-l:i])
            ll[i] = min(low[i-l:i])
        else:
            hh[i] = max(high[:m])
            ll[i] = min(low[:m])
        i +=1
    return hh, ll
    
def is_recent_HL(high, low, hh, ll, K=5):
    is_recentlow = np.zeros(len(low))
    is_recenthigh = np.zeros(len(high))
    for i in range(K, len(high)):
        if (max(high[i-K:i]) >= hh[i]):
            is_recenthigh[i] = 1
        if (min(low[i-K:i]) <= ll[i]):
            is_recentlow[i] = 1
    
    i_rh = is_recenthigh > 0
    i_rl = is_recentlow > 0
    return i_rh, i_rl
    
def is_pullback(high, low, K=5):
    is_low = np.zeros(len(low))
    is_high = np.zeros(len(high))
    for i in range(K, len(high)):
        if (max(high[i-K:i]) <= high[i]):
            is_low[i] = 1
        if (min(low[i-K:i]) >= low[i]):
            is_high[i] = 1
# ! przeanalizuj to !
    i_h = is_high > 0
    i_l = is_low > 0
    
    return i_h, i_l
    
def ror2dolar(ror, position_size = 1.0, holding_period = 3.0, buy=3.00, coc = 0.03, commission_per_lot=50.0):
#all is well with RoR but how much in dollars do you really make? what is your cost of carry? etc.
#This is all just estimation and rule of thumb nothing set in stone
# ror - rate of return, position_size [in lots], holding_periods [in days]
# buy - USDPLN at entry, coc - cost of carry [].
# ror2dolar(0.25)
    lever = 1.0/100     # such is your broker's margin requirement
    lot_size = 100000.0 # you buy and sell 100 000 USD
    # coc [differential of cost of money between currencies] = 3% in anual terms but of the entire lot
    sell = (1+ror)*buy  # logicaly this is your selling price 
    dolar_return = (sell-buy)*lot_size*lever #'dollar' it is not. It's home currency actually
    cost_of_carry = (sell+buy)/2 * (coc/365 * holding_period)*lot_size #average by buy/sell price
    comission = commission_per_lot * position_size            # fixed commision and spread estimated per lot
    net_dollar_profit = dolar_return - cost_of_carry - comission
    return net_dollar_profit, dolar_return, cost_of_carry, comission

