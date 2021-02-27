
import Market
import Asset
import matplotlib.pyplot as plt

from scipy.stats import norm

'''
Example distributions for X and Y
'''
def TestDist(x):
    return norm.cdf(x)    
X = Asset.Asset()
X.setDistribution(TestDist)
Y = Asset.Asset()
Y.setDistribution(TestDist)
'''
Create market and get covariance, efficient frontier, tangency portfolio and minimum variance portfolio with rf set to 20%
'''
S = Market.Market([X,Y], 20)
print('Covariance matrix:')
print(S.getCovarianceMatrix())
print('Minimum variance portfolio:')
print(S.minVariancePortfolio(20))
print('Tangency portfolio:')
print(S.tangencyPortfolio())
S.plotEfficientFrontier(riskless_included=True)
