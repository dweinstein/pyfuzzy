# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Const.py,v 1.9 2008-11-18 21:46:48 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Const(Operator):
    """Special operator which return a constant value.
       
       @ivar value: value returned at call of __call__().
       @type value: float
    """

    def __init__(self,value):
        """Constructor.
        
        @param value: value returned at call of __call__().
        @type value: float
        """
        super(Const, self).__init__()
        self.value = value

    def __call__(self):
        """Return stored constant value."""
        return self.value
