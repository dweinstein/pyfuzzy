from fuzzy.set.Function import Function

class SFunction(Function):

    def __init__(self,a=0.0,delta=1.0):
        Function.__init__(self)
	self.a = a
	self.delta = delta
	
    def __call__(self,x):
        """Return membership of x in this fuzzy set.
	   This function makes the set work like a function."""
        a = self.a
	d = self.delta
	if x<= a-d:
	    return 0.0
	if x<=a:
	    t = (x-a+d)/(2.0*d)
	    return 2.0*t*t    
	if x<=a+d:
	    t = (a-x+d)/(2.0*d)
	    return 1.0-2.0*t*t    
        return 1.0

    def getCOG(self):
	"""Return center of gravity."""
        raise Exception("COG of SFunction uncalculable")

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
                    # maximal interval length
                    stepsize = 2.0*d/Function._resolution
                    if next is None:
                        return min(a+d,prev + stepsize)
                    else:
                        if next - prev > stepsize:
                            # split interval in n equal sized interval of length < stepsize
                            return min(a+d,prev+(next-prev)/(int((next-prev)/stepsize)+1.0))
                        else:
                            return next

    def getIntervalGenerator(self):
        return self.__IntervalGenerator(self)