# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Adjective.py,v 1.7 2008-11-01 13:29:31 rliebscher Exp $"


from fuzzy.norm.Max import Max
from fuzzy.set.Set import Set

class Adjective(object):

    # default if not set in instance
    _COM = Max()

    def __init__(self,set=Set(),COM=None):
        self.set = set
        self.membership = None
        self.COM = COM

    def setMembershipForValue(self,value):
        self.membership = self.set(value)

    def getMembership(self):
        if self.membership is None:
            return 0.0
        else:
            return self.membership

    def setMembership(self,value):
        """Set membership of this adjective, if
           already set use COM norm to merge
           old and new value."""

        if self.membership is None:
            self.membership = value
        else:
            self.membership = (self.COM or self._COM)(
                                                    self.membership,  # consider already set value
                                                    value
                                                )

    def reset(self):
        self.membership = None

    def getName(self,system):
        return system.findAdjectiveName(self)

    def printDot(self,out,system,parent_name,connectToParent=1):
        node_name = parent_name + "_ADJ_" + hex(id(self)).replace('-','_')
        adj = self.getName(system)
        if not(adj is None):
            adjname = adj[1] + "." + adj[0]
        else:
            adjname = "unknown"
        out.write(
"""    %(node_name)s [label="%(adjname)s",shape=box];
""" % {"node_name":node_name,"adjname":adjname})
        if connectToParent:
            out.write(
"""    %(node_name)s -> %(parent_name)s;
""" % {"node_name":node_name,"parent_name":parent_name})
        return node_name
