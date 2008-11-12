# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Const.py,v 1.8 2008-11-12 21:53:40 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Const(Operator):
    """Special operator which return a constant value."""

    def __init__(self,value):
        """Constructor.
        value: value returned at call of __call__()."""
        super(Const, self).__init__()
        self.value = value

    def __call__(self):
        """Return stored constant value."""
        return self.value
