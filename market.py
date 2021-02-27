class Market(object):
    def __init__(self, assets):
        Market.assets = assets
        Market.efficient_frontier
        
    '''Getters'''
    def getAssets(self):
        return Market.assets
    def getCovarianceMatrix(self):
        return