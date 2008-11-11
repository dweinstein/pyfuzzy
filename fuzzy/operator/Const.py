# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Const.py,v 1.7 2008-11-11 12:19:10 rliebscher Exp $"


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

    def printDot(self,out,system,parent_name):
        node_name = parent_name+"_CONST_" + hex(id(self)).replace('-','_')
        out.write(
"""    %(node_name)s [label="%(value)g"];
    %(node_name)s -> %(parent_name)s;
""" % {"node_name":node_name,"value":self.value,"parent_name":parent_name})
        return node_name
