# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Not.py,v 1.10 2008-11-25 14:01:51 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Not(Operator):
    """Take value of input operator and negate it.
       
       @ivar input: input which result is to negate.
       @type input: L{fuzzy.operator.Operator.Operator}
    """ 

    def __init__(self, input):
        """Constructor.
        
        @param input: input which result is to negate.
        @type input: L{fuzzy.operator.Operator.Operator}
        """
        super(Not, self).__init__()
        self.input = input

    def __call__(self):
        """Get input value and return 1.0-value."""
        return 1.0 - self.input()
