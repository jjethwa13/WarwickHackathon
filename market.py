class Market(object):
    def __init__(self, assets):
        Market.assets = assets
        Market.efficient_frontier
        Market.covariance_matrix
        Market.riskless_asset

    '''Getters'''
    def getAssets(self):
        return Market.assets
    def getCovarianceMatrix(self):
        return Market.getCovarianceMatrix

    '''Create riskless asset'''
    def createRisklessAsset(self):
        Market.riskless_asset = Asset()
        return Market.riskless_asset