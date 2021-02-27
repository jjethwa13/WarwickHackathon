import numpy as np
class Market():
    def __init__(self, assets):
        Market.assets = assets
        Market.efficient_frontier
        Market.covariance_matrix = np.diag(np.ones(len(self.assets)))
        Market.riskless_asset

    '''Getters'''
    def get_assets(self):
        return self.assets

    def getCovarianceMatrix(self):
        return self.getCovarianceMatrix

    '''Create riskless asset'''
    def createRisklessAsset(self):
        self.riskless_asset = Asset(rf=0.5)
        return self.riskless_asset

    '''Creates covariance matrix for the assets in the market'''
    def setCovarianceMatrix(self):
        def makeSymmetric(arr):
            return arr + arr.T - np.diag(arr.diagonal())

        for i in range(len(self.assets)):
            for j in range(i):
                self.covariance[j][i]=self.assets[i].getCovariance(self.assets[j])
        return self.covariance_matrix