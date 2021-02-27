##
## Asset Object
##
##

import random
import numpy as np

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
        self.rf = rf
        self.setDistribution(lambda x: int(x >= rf))
        self.price = price
        self.properties = {}
        self.accuracy = 0.01
        
    '''
    Getters
    '''
    def getTimeFrame(self):
        return self.time_frame

    def getDistribution(self):
        return self.distribution

    def getPrice(self):
        return self.price
    
    def getAccuracy(self):
        return self.accuracy
    
    def getProperties(self):
        return self.properties
    
    def getRiskFreeRate(self):
        return self.rf

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
    
    def setAccuracy(self, accuracy):
        self.accuracy = accuracy
    
    def setRiskFreeRate(self, rf):
        self.rf = rf

    def simulate(self, n=1, accuracy=-1):
        '''
        Simulates the returns for the asset
        Will also overwrite the accuracy of the asset's simulation
        
        Parameters :
        n : int (number of datapoints you want to simulate, note that is n=1 the datapoint is returned as a scalar)
        accuracy : float (Determines the step-size when going through the cumulative distribution, a smaller accuracy may decrease performance)
    
        Returns : 
        simulated data : scalar (if n = 1), list (if n > 1)
        
        '''
        if accuracy == -1:
            accuracy = self.accuracy

        X = []

        for _ in range(n):

            x0 = 0

            p = random.random()
            while p == 0:
                p = random.random()

            i = 1
            if p <= self.distribution(x0):      ## We start from 0, i controls whether we decrease x0 or increase
                i = -1
                
            x = x0
            while i*p > i*self.distribution(x):
                x += i*accuracy
            x0 = x
            
            if n == 1:
                return x0
            X.append(x0)
        
        return X
    
    def getExpectation(self):
        
        '''
        Calculates an estimate of the expectation for the asset            
        '''
        return self.getMoment(k=1)
    
    def getVar(self):
        
        '''
        Calculates the variance of the asset
        '''
        
        return (self.getMoment(k=2) - ((self.getMoment(k=1))**2))
    
    def getStd(self):
        
        '''
        Calculates the standard deviation of the asset
        '''
        
        return ((self.getMoment(k=2) - ((self.getMoment(k=1))**2))**(0.5))
    
    def getMoment(self, k=1):
        
        '''
        Gets the k-th moment by using some stupid formula
        '''
        if str(k) in self.properties.keys():
            return self.properties[str(k)]
        
        check = False
        x = 1
        result = 0
        while not check:
            
            item = self.distribution(self.accuracy*(x+1)) - self.distribution(self.accuracy*x)
            item += (-1 ** k)*(self.distribution(self.accuracy*(1-x)) - self.distribution(-1*self.accuracy*x))
            item *= (self.accuracy*x)**k
            result += item
            
            x += 1
            
            check_value = np.abs(self.distribution(self.accuracy*x) + self.distribution(-1*self.accuracy*x) - 1)
            if check_value < 0.0001:
                check = True
        
        self.properties[str(k)] = result
        
        return result
            
        
        
        
        
        
        


    
def Test(x):

    

import matplotlib.pyplot as plt

X = Asset()
X.setDistribution(Test)

print(X.getExpectation())
print(X.getStd())

data = X.simulate(n=10000)
plt.figure(figsize=(20, 10))
plt.hist(data, bins=50)
plt.grid(True)
plt.plot()






