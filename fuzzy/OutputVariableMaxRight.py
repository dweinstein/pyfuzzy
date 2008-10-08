# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariableMaxRight.py,v 1.4 2008-10-08 13:19:17 rliebscher Exp $"


from fuzzy.OutputVariable import OutputVariable
from fuzzy.set.Set import Set,merge,norm
from fuzzy.set.Polygon import Polygon
from fuzzy.norm.Max import Max
from fuzzy.norm.Min import Min

class OutputVariableMaxRight(OutputVariable):
    """Output variable which uses for defuzzyfication
       the right maximum."""

    # default values if instance values are not set 
    _INF = Min()
    _ACC = Max()

    def __init__(self, INF=None, ACC=None, failsafe=None,*args,**keywords):
        OutputVariable.__init__(*tuple([self]+list(args)),**keywords)
        self.ACC = ACC # accumulation
        self.INF = INF # inference
        self.failsafe = failsafe # which value if value not calculable
        
    def getValue(self):
        """Defuzzyfication."""
        temp = None
        for adjective in self.adjectives.values():
            # get precomputed adjective set
            temp2 = norm((self.INF or self._INF),adjective.set,adjective.getMembership())
            # accumulate all adjectives
            if temp is None:
                temp = temp2
            else:
                temp = merge((self.ACC or self._ACC),temp,temp2)
        
	# get polygon representation
	ig = temp.getIntervalGenerator()
	next = ig.nextInterval(None,None)
	x = None
	y = None
	while next is not None:
	    x_ = next
	    y_ = temp(x_)
	    if x is None:
	 	y = y_
		x = x_
	    if y_ >= y:
		y = y_
		x = x_
	    # get next point from polygon
	    next = ig.nextInterval(next,None)
	# right end of polygon is maximum then it goes to infinity
	if y is not None and y_ >= y:
	    x = float('inf')

        # was not to calculate
	if x is None and self.failsafe is not None:
            # user gave us a value to return 
            return self.failsafe
	return x
