class Market(object):
    def __init__(self, assets):
        Market.assets = assets
        Market.efficient_frontier
        Market.covariance_matrix

    '''Getters'''
    def getAssets(self):
        return Market.assets
    def getCovarianceMatrix(self):
        return Market.getCovarianceMatrix