# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Not.py,v 1.5 2008-10-24 20:47:09 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Not(Operator):
    """Take value of input operator and negate it.""" 

    def __init__(self, input):
        """Constructor.
        input:  input which result is to negate."""
        Operator.__init__(self)
        self.input = input

    def __call__(self):
        """Get input value and return 1.0-value."""
        return 1.0 - self.input()

    def printDot(self,system,parent_name):
        node_name = parent_name+"_NOT_" + hex(hash(self)).replace('-','_')
        print """
    %(node_name)s [label="NOT"];
    %(node_name)s -> %(parent_name)s;
""" % {"node_name":node_name,"parent_name":parent_name}
        self.input.printDot(system,node_name)
        return node_name
