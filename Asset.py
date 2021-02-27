##
## Asset Object
##
##

import random

class Asset(object):

    def __init__(self, timeframe=-1, rf=0.0, price=1):

        '''
        Init function
        Parameters :
            timeframe : int (Denotes the operable timeframe for the asset)
            riskless : bool (Denotes whether this will be a riskless asset or not)
            rf : float (Denotes the risk-free rate for the riskless asset)
        '''

        self.time_frame = timeframe
        self.setDistribution(lambda x: int(x >= rf))
        self.price = price
        
    '''
    Getters
    '''
    def getTimeFrame(self):
        return self.time_frame

    def getDistribution(self):
        return self.distribution

    def getPrice(self):
        return self.price

    '''
    Setters
    '''

    def setDistribution(self, func):
        '''
        Sets the Asset with a distribution
        Note that this distribution function must be a valid cumulative distribution
    
        '''
        self.distribution = func

    def setTimeFrame(self, timeframe):
        self.time_frame = timeframe

    def setPrice(self, price):
        self.price = price

    def simulate(self, n=1, accuracy=0.01):
        '''
        Simulates the returns for the asset
        '''

        X = []

        for _ in range(n):

            x0 = 0

            p = random.random()
            while p == 0:
                p = random.random()

            i = 1
            if p <= self.distribution(x0):
                i = -1

            if increasing:
                x = x0
                while i*p > i*self.distribution(x):
                    x += i*accuracy
                x0 = x
            
            if n == 1:
                return x0
            X.append(x0)
        
        return X


    
def Test(x):

    if x < 0:
        return 0.0
    elif x < 1:
        return 0.10
    elif x < 2:
        return 0.40
    elif x < 3:
        return 0.50
    elif x < 5:
        return 0.90
    elif x < 6:
        return 0.95
    else:
        return 1.0

import matplotlib.pyplot as plt

X = Asset()
X.setDistribution(Test)
data = X.simulate(n=1000)

plt.figure(figsize=(20, 10))
plt.hist(data, bins=15)
plt.grid(True)
plt.plot()






