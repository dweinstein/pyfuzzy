# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Compound.py,v 1.9 2008-11-18 21:46:48 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Compound(Operator):
    """Take values of input operators  and process them
       through the given norm.

       @ivar norm: how to combine inputs. (eg. Min,Max,...)
       @type norm: instance of L{fuzzy.norm.Norm.Norm}
       @ivar inputs: list of inputs (subclassed from L{fuzzy.operator.Operator.Operator}).
    """ 

    def __init__(self, norm, *inputs):
        """Constructor.
        
        @param norm: how to combine inputs. (eg. Min,Max,...)
        @type norm: instance of L{fuzzy.norm.Norm.Norm}
        @param inputs: list of inputs (subclassed from L{fuzzy.operator.Operator.Operator}).
        """
        super(Compound, self).__init__()
        self.norm = norm
        self.inputs = inputs

    def __call__(self):
        """Get current value of input and combine them with help of norm."""
        return self.norm(*[x() for x in self.inputs])
