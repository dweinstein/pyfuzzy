"""
Base class for all fuzzy sets.
Helper function for calculation with fuzzy sets.

----
Intersection of set1 and set2 can be done by

set = merge(T_NORM,set1,set2)

where T_NORM is a t-norm eg. Min.
(or a function which accepts two parameters as min().)

----
Union of set1 and set2 can be done by

set = merge(S_NORM,set1,set2)

where S_NORM is a s-norm eg. Max.
(or a function which accepts two parameters as max().)

----
Negation of set1 can be done by

set = norm(lambda a,b:1.0-a ,set1,0.0)

using a user defined function for it.
(The second parameter is ignored or better said
it doesn't influence the value, it only influences
maybe where the points of the resulting polygon are
set.)
"""

# helper functions
def _find_null_steffensen(x,f,epsilon=None):
    """Find null point of function f by using the Steffensen method.
       As fixpoint equation g(x) = x - f(x) is used.
       The algorithm stops if the error estimation is smaller than epsilon
       or the convergence quotient is larger than 1.0 (for at least two steps)
       or there is an ZeroDivisionError, which means in the last steps
       nothing changed.

       Normally the number of correct digits doubles each step, which
       means for 64 bits it needs not more than 6-7 steps for an
       arbitrary function.
    """
    g = lambda x,f=f: x-f(x)    
    x_2,x_1,x_0 = None,None,x
    q_0,q_1 = 0.0,0.0
    e = None
    while abs(q_0)<1.0 or abs(q_1)<1.0:
        y0 = x_0
        y1 = g(y0)
        y2 = g(y1)
        try:
            x_2,x_1,x_0 = x_1,x_0,y2 - (y2-y1)*(y2-y1)/(y2-2*y1+y0)
            if x_2 is not None:
                # Konvergenzquotient
                q_1,q_0 = q_0,(x_0-x_1)/(x_1-x_2)
                if epsilon is not None:
                    # Fehlerschaetzung
                    if epsilon > abs((x_0-x_1)*(x_0-x_1)/(x_0-2*x_1+x_2)):
                        break
        except ZeroDivisionError:
            break
    return x_0


def merge(NORM, set1, set2):
	"""Returns a new fuzzy set which the merger of set1 and set2,
	   where the resulting membership is equal to NORM(set1(x),set2(x))."""
	from fuzzy.set.Polygon import Polygon
	ret = Polygon()
	
	g1 = set1.getIntervalGenerator()
	g2 = set2.getIntervalGenerator()
	
	x = g1.nextInterval(None,None)
	x_ = g2.nextInterval(None,x)
	if x_ is not None and x_ < x:
	    x = x_
	if x is None:
	    return ret
	y1 = set1(x)
	y2 = set2(x)
	ret.add(x=x,y=NORM(y1,y2))
	cached_x, cached_y1, cached_y2 = None, None, None
	while 1:
	    # add this point
	    ret.add(x,NORM(y1,y2))
	    prev_x, prev_y1, prev_y2 = x, y1, y2
	    # check if there is something left from a previous split interval
	    if cached_x is not None:
		x, y1, y2 = cached_x, cached_y1, cached_y2
	        cached_x, cached_y1, cached_y2 = None, None, None
	    else:
		# get new interval from sets
		x = g1.nextInterval(prev_x,None)
		x_ = g2.nextInterval(prev_x,x)
		if x_ is not None and x_ < x:
	            x = x_
	        if x is None: # no need for more intervals
		    break
		y1 = set1(x)
		y2 = set2(x)
		# test if intersection => split interval
		if (x != prev_x) and ((y1>y2 and prev_y1<prev_y2) or (y1<y2 and prev_y1>prev_y2)):
		    # calculate intersection
		    y_diff = y1-y2
		    prev_y_diff = prev_y2-prev_y1
		    p = prev_y_diff/(prev_y_diff + y_diff)
		    cached_x, cached_y1, cached_y2 = x, y1, y2
		    x = prev_x + p * (x-prev_x)
		    if not (isinstance(set1,Polygon)
                       and isinstance(set2,Polygon)):
                        # in this case we have only an approximation
                        x = _find_null_steffensen(x,lambda x,set1=set1,set2=set2:set1(x)-set2(x))
		    y1 = set1(x)
		    y2 = set2(x)
	return ret

def norm(NORM, set, value):
        """Returns a new fuzzy set which this set normed with value."""
	from fuzzy.set.Polygon import Polygon
	ret = Polygon()
	
	g = set.getIntervalGenerator()
	
	x = g.nextInterval(None,None)
	if x is None:
	    return ret
	y = set(x)
	ret.add(x=x,y=NORM(y,value))
	cached_x, cached_y = None, None
	while 1:
	    # add this point
	    ret.add(x,NORM(y,value))
	    prev_x, prev_y = x, y
	    # check if there is something left from a previous split interval
	    if cached_x is not None:
		x, y = cached_x, cached_y
	        cached_x, cached_y = None, None
	    else:
		# get new interval from sets
		x = g.nextInterval(prev_x,None)
	        if x is None: # no need for more intervals
		    break
		y = set(x)
		# test if intersection => split interval
		if (x != prev_x) and ((y>value and prev_y<value) or (y<value and prev_y>value)):
		    # calculate intersection
		    y_diff = y-value
		    prev_y_diff = value-prev_y
		    p = prev_y_diff/(prev_y_diff + y_diff)
		    cached_x, cached_y = x, y
		    x = prev_x + p * (x-prev_x)
		    if not isinstance(set,Polygon):
                        # in this case we have only an approximation
                        x = _find_null_steffensen(x,lambda x,set=set,value=value:set(x)-value)
		    y = set(x)
	return ret



class Set:   

   def __init__(self):
        """Dummy initialization, so it is safe to call it
	   from any sub class."""  
        pass

   def __call__(self,x):
        """Return membership of x in this fuzzy set.
	   This function makes the set work like a function."""
        return 0
        
   class IntervalGenerator:
	def nextInterval(self,prev,next):
	    """For conversion of any set to a polygon representation.
	       Return which end value should have the interval started
	       by prev. (next is the current proposal.)
	       The membership function has to be monotonic in this interval.
	       (eg. no minima or maxima)
	       To find left start point prev is None.
	       If no further splitting at right necessary return None."""
	    return next

   def getIntervalGenerator(self):
	return self.IntervalGenerator()

   def getCOG(self):
	"""Return center of gravity."""
        #raise Exception("abtract class %s has no center of gravity." % self.__class__.__name__)
	return 0 # XXX
	
	