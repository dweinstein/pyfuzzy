# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Not.py,v 1.4 2008-10-08 13:14:45 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Not(Operator):
    """Take value of input operator and negate it.""" 
    
    def __init__(self, input):
	"""Constructor.
	input:	input which result is to negate."""
        Operator.__init__(self)
        self.input = input

    def __call__(self):
	"""Get input value and return 1.0-value."""
        return 1.0 - input()

