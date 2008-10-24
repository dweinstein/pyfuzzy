# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Compound.py,v 1.5 2008-10-24 20:47:09 rliebscher Exp $"


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
        Operator.__init__(self)
        self.norm = norm
        self.inputs = inputs

    def __call__(self):
        """Get current value of input and combine them with help of norm."""
        return apply(self.norm,map(lambda x:x(),self.inputs))

    def printDot(self,system,parent_name):
        norm_name = self.norm.printDot(system,parent_name)
        for i in self.inputs:
            i.printDot(system,norm_name)
        return norm_name

