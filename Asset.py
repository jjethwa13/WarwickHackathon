##
## Asset Object
##
##

class Asset(object):

    def __init__(self, timeframe = -1):

        '''
        Init function
        Parameters : 
            timeframe : int (Denotes the operable timeframe for the asset)
        '''

        self.TimeFrame = timeframe
        
    '''
    Getters
    '''
    def getTimeFrame(self):
        return self.TimeFrame

    def setDistribution(self, func):
        self.Distribution = 







