from fuzzy.set.Polygon import Polygon

class Triangle(Polygon):
    """Triangle shaped fuzzy set."""

    def __init__(self,y_max=1.0,y_min=0.0,m=0.0,alpha=1.0,beta=1.0):
	"""Constructor.
	y_max:	y-value at top of the triangle (1.0)
	y_min:  y-value outside the triangle (0.0)
	m:	x-value of top of triangle (0.0)
	alpha:	distance of left corner to m (1.0)
	beta:	distance of right corner to m (1.0)
	"""
        Polygon.__init__(self)
	# don't trigger __setattr__
	self.__dict__["y_max"] = y_max
	self.__dict__["y_min"] = y_min
	self.__dict__["m"] = m
	self.__dict__["alpha"] = alpha
	self.beta = beta # update polygon
	
    def __setattr__(self,name,value):
        self.__dict__[name] = value
	if name in ["y_max",
			"y_min",
			"m",
			"alpha",
			"beta"]:
	    # update polygon
	    Polygon.clear(self)
	    Polygon.add(self,self.m-self.alpha,self.y_min)    
	    Polygon.add(self,self.m,self.y_max)    
	    Polygon.add(self,self.m+self.beta,self.y_min)    
	    	
    def add(self,x,y,where=Polygon.END):
	"""Don't let anyone destroy our triangle."""
	raise Exception()

    def remove(self,x,where=Polygon.END):
	"""Don't let anyone destroy our triangle."""
	raise Exception()

    def clear(self):
	"""Don't let anyone destroy our triangle."""
	raise Exception()

