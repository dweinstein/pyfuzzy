# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Not.py,v 1.7 2008-11-11 12:19:11 rliebscher Exp $"


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

    def printDot(self,out,system,parent_name):
        node_name = parent_name+"_NOT_" + hex(id(self)).replace('-','_')
        out.write(
"""    %(node_name)s [label="NOT"];
    %(node_name)s -> %(parent_name)s;
""" % {"node_name":node_name,"parent_name":parent_name})
        self.input.printDot(out,system,node_name)
        return node_name
