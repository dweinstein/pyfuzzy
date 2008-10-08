# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Input.py,v 1.4 2008-10-08 13:14:45 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Input(Operator):
    """Special operator which gets it value from a fuzzy adjective."""

    def __init__(self,adjective):
	"""Constructor.
	adjective: from which adjective get the membership value.""" 
        Operator.__init__(self)
        self.adjective = adjective

    def __call__(self):
	"""return membership of given adjective."""
        return self.adjective.getMembership()        

