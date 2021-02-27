
import Market
import Asset
import matplotlib.pyplot as plt



    

    
X = Asset.Asset()
X.setDistribution(TestDist)

Y = Asset.Asset()
Y.setDistribution(TestDist2)

#S = Market.Market([X,Y], 0.01)
#
#print(S.getCovarianceMatrix())

print(X.simulate(n=10000))

#print(X.getCovar(Y))


















