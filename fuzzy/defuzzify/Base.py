# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Base.py,v 1.1 2008-11-11 12:50:02 rliebscher Exp $"


from fuzzy.norm.Max import Max
from fuzzy.norm.Min import Min
from fuzzy.set.Set import norm,merge

class Base(object):
    """Abstract base class for defuzzyfication
       which results in a numeric value."""

    # default values if instance values are not set 
    _INF = Min()
    _ACC = Max()

    def __init__(self, INF=None, ACC=None):
        """
            INF - inference norm, used with set of adjective and given value for it
            ACC - norm for accumulation of set of adjectives
        """ 
        self.ACC = ACC # accumulation
        self.INF = INF # inference

    def accumulate(self,variable):
        """combining adjective values into one set"""
        temp = None
        for adjective in variable.adjectives.values():
            # get precomputed adjective set
            temp2 = norm((self.INF or self._INF),adjective.set,adjective.getMembership())
            # accumulate all adjectives
            if temp is None:
                temp = temp2
            else:
                temp = merge((self.ACC or self._ACC),temp,temp2)
        return temp

    def value_table(self,set):
        """get a value table of the polygon representation"""
        # get polygon representation
        ig = set.getIntervalGenerator()
        next = ig.nextInterval(None,None)
        while next is not None:
            x = next
            y = set(x)
            yield (x,y)
            # get next point from polygon
            next = ig.nextInterval(next,None)
