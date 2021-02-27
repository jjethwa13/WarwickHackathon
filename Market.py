import numpy as np
class Market():
    def __init__(self, assets, rf):
        '''
        Parameters :
            assets : list (List of asset objects defined in Asset.py)
            rf : float (Denotes the risk-free rate for the riskless asset)
        '''
        self.assets = assets
        self.efficient_frontier

        self.covariance_matrix = np.diag(np.ones(len(self.assets)))
        setCovarianceMatrix()
        self.inv_covariance_matrix
        setInvCovarianceMatrix()

        self.riskless_asset
        self.expected_returns = [asset.getExpectation() for asset in assets]
        self.tangency_portfolio
        self.rf = rf

    '''
    Getters
    '''
    def get_assets(self):
        return self.assets

    def getCovarianceMatrix(self):
        return self.getCovarianceMatrix

    
    def createRisklessAsset(self):
        '''
        Creates riskless asset using the risk free rate
        '''
        self.riskless_asset = Asset(rf=self.rf)
        return self.riskless_asset

    '''
    Creates covariance matrix for the assets in the market
    '''
    def setCovarianceMatrix(self):   
        def makeSymmetric(arr):
            return arr + arr.T - np.diag(arr.diagonal())

        for i in range(len(self.assets)):
            for j in range(i):
                self.covariance[j][i]=self.assets[i].getCovariance(self.assets[j])
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
        calcConstants()
        
        a = np.matmul(self.inv_covariance_matrix,self.expected_returns-self.rf*np.ones(len(self.expected_returns)))
        self.tangency_portfolio = a/(self.B-self.rf*self.A)
        return self.tangency_portfolio
    
    def calcConstants(self):
        if (self.A==None):
            ones = np.ones(len(self.assets))
            self.A = np.matmul(ones,np.matmul(self.inv_covariance_matrix,ones))
        if (self.B == None):
            ones = np.ones(len(self.assets))
            self.B = np.matmul(ones,np.matmul(self.inv_covariance_matrix,self.expected_returns))
        return 0

    def efficientFrontier(self,mean):
        '''
        Takes mean as argument and returns Variance
        '''
        calcConstants()
        variance = (mean-self.rf)**2/()