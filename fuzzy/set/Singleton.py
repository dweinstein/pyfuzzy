# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Singleton.py,v 1.4 2008-10-08 13:15:22 rliebscher Exp $"


from fuzzy.set.Polygon import Polygon

# use Polygon as base class so we dont need write all
# methods again
class Singleton(Polygon):
    """This set represents a non-fuzzy number."""

    def __init__(self,x=0.0):
        Polygon.__init__(self)
	self.x = x # update polygon
	
    def __setattr__(self,name,value):
        self.__dict__[name] = value
	if name in ["x"]:
	    # update polygon
	    Polygon.clear(self)
	    Polygon.add(self,self.x,0.0)    
	    Polygon.add(self,self.x,1.0)    
	    Polygon.add(self,self.x,0.0)    
	    	
    def __call__(self,x):
	"""Get membership of value x."""
	if x == self.x:
	    return 1.0
	else:
	    return 0.0

    def getCOG(self):
	"""Return center of gravity."""
        return self.x

    def add(self,x,y,where=Polygon.END):
	"""Don't let anyone destroy our singleton."""
	raise Exception()

    def remove(self,x,where=Polygon.END):
	"""Don't let anyone destroy our singleton."""
	raise Exception()

    def clear(self):
	"""Don't let anyone destroy our singleton."""
	raise Exception()
	
