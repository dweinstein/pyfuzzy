# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Variable.py,v 1.9 2008-11-18 18:55:06 rliebscher Exp $"


class Variable(object):
    """Base class for any kind of fuzzy variable.
       Returns as output the previous input value."""

    def __init__(self,description='',min=0.,max=1.,unit=''):
        """
            @param description: Description of the fuzzy variable
            @type description: string
            @param min: minimum value (not strictly enforced, but useful for some external tools)
            @type min: float
            @param max: maximum value (not strictly enforced, but useful for some external tools)
            @type max: float
            @param unit: Unit of the values
            @type unit: string
        """
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

    def reset(self):
        """Reset meberships of adjectives for new calculation step."""
        for adjective in self.adjectives.values():
            adjective.reset()

    def getName(self,system):
        """Lookup the name given this variable in the given system"""
        return system.findVariableName(self)
