
__revision__ = "$Id: OutputVariableMaxLeft.py,v 1.3 2003-04-14 08:49:32 rliebscher Exp $"


from fuzzy.OutputVariable import OutputVariable
from fuzzy.set.Set import Set,merge,norm
from fuzzy.set.Polygon import Polygon
from fuzzy.norm.Max import Max
from fuzzy.norm.Min import Min

class OutputVariableMaxLeft(OutputVariable):
    """Output variable which uses for defuzzyfication
       the left maximum."""

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
		x = float('-inf') # left end of polygon is always -infinity
	    if y_ > y:
		y = y_
		x = x_
	    # get next point from polygon
	    next = ig.nextInterval(next,None)

        # was not to calculate
    
	if x is None and self.failsafe is not None:
            # user gave us a value to return 
            return self.failsafe
	return x
