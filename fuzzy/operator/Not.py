# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Not.py,v 1.9 2008-11-18 21:46:48 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Not(Operator):
    """Take value of input operator and negate it.
       
       @ivar input: input which result is to negate.
       @type input: instance of L{fuzzy.operator.Operator.Operator}
    """ 

    def __init__(self, input):
        """Constructor.
        
        @param input: input which result is to negate.
        @type input: instance of L{fuzzy.operator.Operator.Operator}
        """
        super(Not, self).__init__()
        self.input = input

    def __call__(self):
        """Get input value and return 1.0-value."""
        return 1.0 - self.input()
