# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariableCOG.py,v 1.7 2008-10-08 13:19:17 rliebscher Exp $"


from fuzzy.OutputVariable import OutputVariable
from fuzzy.set.Set import Set,merge,norm
from fuzzy.set.Polygon import Polygon
from fuzzy.norm.Max import Max
from fuzzy.norm.Min import Min

class OutputVariableCOG(OutputVariable):
    """Output variable which uses for defuzzyfication
       the center of gravity method."""

    # default values if instance values are not set 
    _INF = Min()
    _ACC = Max()

    def __init__(self, INF=None, ACC=None, failsafe=None,*args,**keywords):
	"""
	    INF - inference norm, used with set of adjective and given value for it
	    ACC - norm for accumulation of set of adjectives
	    failsafe - if is not possible to calculate a center of gravity,
			return this value if not None
			or forward the exception
	""" 
        OutputVariable.__init__(*tuple([self]+list(args)),**keywords)
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
            if self.failsafe is not None:
                # user gave us a value to return
                return self.failsafe
            else:
                # forward exception
                raise e