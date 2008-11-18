# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: PiFunction.py,v 1.12 2008-11-18 21:46:48 rliebscher Exp $"


from fuzzy.set.Function import Function
from fuzzy.set.SFunction import SFunction
from fuzzy.set.ZFunction import ZFunction

class PiFunction(Function):
    r"""
    Realize a Pi-shaped fuzzy set::
        
                _
               /|\
              / | \
            _/  |  \_
             |  a  |
             |     |
             2*delta

    See also U{http://pyfuzzy.sourceforge.net/test/set/PiFunction.png}

    
    @ivar a: center of set.
    @type a: float
    @ivar delta: absolute distance between x-values for minimum and maximum.
    @type delta: float
    """

    def __init__(self,a=0.0,delta=1.0):
        """Initialize a Pi-shaped fuzzy set.

        @param a: center of set
        @type a: float
        @param delta: absolute distance between x-values for minimum and maximum
        @type delta: float
        """
        super(PiFunction,self).__init__()
        self.a = a
        self.delta = delta

    def __call__(self,x):
        """Return membership of x in this fuzzy set.
           This method makes the set work like a function.
           
           @param x: value for which the membership is to calculate
           @type x: float
           @return: membership
           @rtype: float
           """
        a = self.a
        d = self.delta/2.0
        if x < a:
            return SFunction(a-d,d)(x)
        else:
            return ZFunction(a+d,d)(x)

    def getCOG(self):
        """Return center of gravity."""
        return self.a

    class __IntervalGenerator(Function.IntervalGenerator):
        def __init__(self,set):
            self.set = set

        def nextInterval(self,prev,next):
            a = self.set.a
            d = self.set.delta
            if prev is None:
                if next is None:
                    return a-d
                else:
                    return min(next,a-d)
            else:
                # right of our area of interest
                if prev >= a+d:
                    return next
                else:
                    # dont forget we have a maximum
                    if prev >= a:
                        consider_this = a + d
                    else:
                        consider_this = a
                    # maximal interval length
                    stepsize = d/Function._resolution
                    if next is None:
                        return min(consider_this,prev + stepsize)
                    else:
                        if next - prev > stepsize:
                            # split interval in n equal sized interval of length < stepsize
                            return min(consider_this,prev+(next-prev)/(int((next-prev)/stepsize)+1.0))
                        else:
                            return next

    def getIntervalGenerator(self):
        return self.__IntervalGenerator(self)
