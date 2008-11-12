# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Compound.py,v 1.8 2008-11-12 21:53:40 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Compound(Operator):
    """Take values of input operators  and process them
       through the given norm.
    """ 

    def __init__(self, norm, *inputs):
        """Constructor.
        norm:   how combine inputs. (eg. Min,Max,...)
        inputs: list of inputs (subclassed from Operator).
        """
        super(Compound, self).__init__()
        self.norm = norm
        self.inputs = inputs

    def __call__(self):
        """Get current value of input and combine them with help of norm."""
        return self.norm(*[x() for x in self.inputs])
