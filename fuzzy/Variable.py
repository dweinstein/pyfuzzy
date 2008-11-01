# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Variable.py,v 1.7 2008-11-01 13:29:31 rliebscher Exp $"


class Variable(object):
    """Base class for any kind of fuzzy variable.
       Returns as output the previous input value."""

    def __init__(self,description='',min=0.,max=1.,unit=''):
        self.adjectives = {}
        self.__value     = None
        self.description = description
        self.min         = min
        self.max         = max
        self.unit        = unit

    def setValue(self,value):
        """Let adjectives calculate their membership values."""
        self.__value = value
        for adjective in self.adjectives.values():
            adjective.setMembershipForValue(value)

    def getValue(self):
        """Return previous input value."""
        return self.__value

    def setDescription(self,description):
        """Set Variable description."""
        self.description = description

    def getDescription(self):
        """Return Variable description."""
        return self.description

    def setMin(self,min):
        """Set Variable minimum value."""
        self.min = min

    def getMin(self):
        """Return Variable minimum."""
        return self.min

    def setMax(self,max):
        """Set Variable minimum value."""
        self.max = max

    def getMax(self):
        """Return Variable minimum."""
        return self.max
    
    def setUnit(self,unit):
        """Set Variable unit."""
        self.unit = unit

    def getUnit(self):
        """Return Variable unit."""
        return self.unit

    def reset(self):
        """Reset meberships of adjectives for new calculation step."""
        for adjective in self.adjectives.values():
            adjective.reset()

    def getName(self,system):
        """Lookup the name given this variable in the given system"""
        return system.findVariableName(self)

    def printDot(self,out,system,name):
        node_name = "VAR_" + hex(id(self)).replace('-','_')
        out.write(
"""    subgraph "%(node_name)s" {
    label="%(name)s";
    %(node_name)s [label="%(name)s"];
""" % {"node_name":node_name,"name":name})
        for adj in self.adjectives.values():
            adj.printDot(out,system,node_name,1)
        out.write(
"""}
""")
