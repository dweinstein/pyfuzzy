
__revision__ = "$Id: ZFunction.py,v 1.4 2003-06-11 13:29:12 rliebscher Exp $"


from fuzzy.set.SFunction import SFunction

class ZFunction(SFunction):
    """Z shaped fuzzy set.""" 

    def __init__(self,a=0.0,delta=1.0):
	"""
	   __
             \     
             |\ 
             | \      
             | |\ 
             | | \__
             | a |
             |   |
             delta  

	http://rene-liebscher.info/PyFuzzy/pyfuzzy/test/set/ZFunction.png

	"""
        SFunction.__init__(self,a,delta)


    def __call__(self,x):
        """Return membership of x in this fuzzy set.
	   This function makes the set work like a function."""
        return 1.0 - SFunction.__call__(self,x)
        
