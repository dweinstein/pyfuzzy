from fuzzy.Variable import Variable
from fuzzy.set.Set import Set,merge,norm
from fuzzy.set.Polygon import Polygon
from fuzzy.norm.Max import Max
from fuzzy.norm.Min import Min

class OutputVariableCOG(Variable):
    """Output variable which uses for defuzzyfication
       the center of gravity method."""

    # default values if instance values are not set 
    _INF = Min()
    _ACC = Max()

    def __init__(self, INF=None, ACC=None, failsafe=None):
        Variable.__init__(self)
        self.ACC = ACC # accumulation
        self.INF = INF # inference
        self.failsafe = failsafe # which value if COG not calculable
        
    def getValue(self):
        """Defuzzyfication using center of gravity method."""
        temp = None
        for adjective in self.adjectives.values():
            # get precomputed adjective set
            temp2 = norm((self.INF or self._INF),adjective.set,adjective.getMembership())
            # accumulate all adjectives
            if temp is None:
                temp = temp2
            else:
                temp = merge((self.ACC or self._ACC),temp,temp2)
        try:
            return temp.getCOG()
        except Exception,e:
            # was not to calculate
            if self.failsafe:
                # user gave us a value to return 
                return self.failsafe
            else:
                # forward exception
                raise e