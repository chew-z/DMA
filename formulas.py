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