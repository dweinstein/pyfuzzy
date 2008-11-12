# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Not.py,v 1.8 2008-11-12 21:53:40 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Not(Operator):
    """Take value of input operator and negate it.""" 

    def __init__(self, input):
        """Constructor.
        input:  input which result is to negate."""
        super(Not, self).__init__()
        self.input = input

    def __call__(self):
        """Get input value and return 1.0-value."""
        return 1.0 - self.input()
