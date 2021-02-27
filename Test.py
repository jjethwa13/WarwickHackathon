
import Market
import Asset
import matplotlib.pyplot as plt

from scipy.stats import norm

def TestDist(x):
    return norm.cdf(x)
    
X = Asset.Asset()
X.setDistribution(TestDist)

Y = Asset.Asset()
Y.setDistribution(TestDist)

S = Market.Market([X,Y], 21)
print(S.getCovarianceMatrix())
S.plotEfficientFrontier(riskless_included=True)
