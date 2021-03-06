import numpy as np
import matplotlib.pyplot as plt
from Asset import *

class Market():
    def __init__(self, assets, rf):
        '''
        Parameters :
            assets : list (List of asset objects defined in Asset.py)
            rf : float (Denotes the risk-free rate for the riskless asset)
        '''
        self.assets = assets
        

        self.covariance_matrix = np.diag(np.ones(len(self.assets)))
        self.setCovarianceMatrix()
        self.setInvCovarianceMatrix()
        
        self.expected_returns = [asset.getExpectation() for asset in assets]
        self.rf = rf
        self.createRisklessAsset()
        self.A=None
        self.B=None
        self.C=None

    '''
    Getters
    '''
    def get_assets(self):
        return self.assets

    def getCovarianceMatrix(self):
        return self.covariance_matrix

    
    def createRisklessAsset(self):
        '''
        Creates riskless asset using the risk free rate
        '''
        self.riskless_asset = Asset(rf=self.rf)
        return self.riskless_asset

    
    def setCovarianceMatrix(self): 
        '''
        Creates covariance matrix for the assets in the market
        '''  
        def makeSymmetric(arr):
            return arr + arr.T - np.diag(arr.diagonal())

        for i in range(len(self.assets)):
            for j in range(i):
                self.covariance_matrix[j][i] = self.assets[i].getCovar(self.assets[j])
        
        self.covariance_matrix = makeSymmetric(self.covariance_matrix)
        return self.covariance_matrix
    
    def setInvCovarianceMatrix(self):
        self.inv_covariance_matrix = np.linalg.inv(self.covariance_matrix)
        return self.inv_covariance_matrix

    def minVariancePortfolio(self, mean):
        '''
        Calculates the minimum variance portfolio
        '''
        a = self.expected_returns-self.rf*np.ones(len(self.expected_returns))
        b = np.matmul(self.inv_covariance_matrix,a)
        min_variance_portfolio = ((mean-self.rf)*b)/np.matmul(a,b)
        return min_variance_portfolio

    def tangencyPortfolio(self):
        '''
        Calculates the Markowitz tangency portfolio
        '''
        self.calcConstants()
        ones = np.ones(len(self.assets))
        a = np.matmul(self.inv_covariance_matrix,self.expected_returns-self.rf*np.ones(len(self.expected_returns)))
        self.tangency_portfolio = a/(self.B-self.rf*self.A)
        return self.tangency_portfolio
    
    def calcConstants(self):
        '''
        Calculates constants that are used within various portfolio calculations
        '''
        if (self.A==None):
            ones = np.ones(len(self.assets))
            self.A = np.matmul(ones,np.matmul(self.inv_covariance_matrix,ones))
        if (self.B == None):
            ones = np.ones(len(self.assets))
            self.B = np.matmul(ones,np.matmul(self.inv_covariance_matrix,self.expected_returns))
        if (self.C == None):
            self.C = np.matmul(self.expected_returns,np.matmul(self.inv_covariance_matrix,self.expected_returns))
        return 0

    def efficientFrontier(self,mean, riskless_included = False):
        '''
        Takes mean as argument and returns variance
        '''
        self.calcConstants()
        ones = np.ones(len(self.assets))
        #a = np.matmul(self.inv_covariance_matrix,self.expected_returns-self.rf*np.ones(len(self.expected_returns)))
        if riskless_included:
            return ((mean-self.rf)**2)/(self.A*self.rf**2-2*self.B*self.rf+self.C) #Variance
        else:
            return (self.A*mean**2-2*self.B*mean+self.C)/(self.A*self.C-self.B**2) 
    
    def plotEfficientFrontier(self, riskless_included=False):
        '''
        Plots the efficient frontier using the efficientFrontier function
        '''
        self.calcConstants()
        if riskless_included:
            mean_axis = np.linspace(self.rf, self.rf+1,num=100)
            zero = self.efficientFrontier(self.rf)
            for mean in mean_axis:
                frontier = self.efficientFrontier(mean, riskless_included=riskless_included)
                plt.scatter(frontier, mean)
                plt.scatter(frontier, self.rf-(mean-self.rf))
            plt.show()
        else:
            mean_axis = np.linspace(self.B/self.A, (self.B/self.A)+1,num=100)
            for mean in mean_axis:
                frontier = self.efficientFrontier(mean, riskless_included=riskless_included)
                plt.scatter(frontier,- mean)
                plt.scatter(frontier,- (self.B/self.A-(mean-self.B/self.A)))
            plt.show()
        