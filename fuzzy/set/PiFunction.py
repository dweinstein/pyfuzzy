
__revision__ = "$Id: PiFunction.py,v 1.4 2003-06-11 13:29:11 rliebscher Exp $"


from fuzzy.set.Function import Function
from fuzzy.set.SFunction import SFunction
from fuzzy.set.ZFunction import ZFunction

class PiFunction(Function):
    """Pi shaped fuzzy set."""

    def __init__(self,a=0.0,delta=1.0):
	"""
               ^
              /|\ 
            _/ | \_
             | a |
             |   |
            2*delta  

	http://rene-liebscher.info/PyFuzzy/pyfuzzy/test/set/PiFunction.png

	"""
        Function.__init__(self)
	self.a = a
	self.delta = delta

    def __call__(self,x):
        """Return membership of x in this fuzzy set.
	   This function makes the set work like a function."""
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