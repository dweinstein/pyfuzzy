# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Adjective.py,v 1.11 2008-11-25 14:01:51 rliebscher Exp $"


from fuzzy.norm.Max import Max
from fuzzy.set.Set import Set

class Adjective(object):
    """Describes a ... of a variable.
    
    @ivar set: fuzzy set
    @type set: L{fuzzy.set.Set.Set}
    @ivar COM: norm (if None the class default _COM is used.)
    @type COM: L{fuzzy.norm.Norm.Norm}
    @ivar membership: set or calculated membership
    @type membership: float
    @cvar _COM: class default is instance variable is None
    @type _COM: L{fuzzy.norm.Norm.Norm}
    """

    # default if not set in instance
    _COM = Max()

    def __init__(self,set=Set(),COM=None):
        """Initialize adjective.
        
        @param set: fuzzy set
        @type set: L{fuzzy.set.Set.Set}
        @param COM: norm (if None the class default _COM is used.)
        @type COM: L{fuzzy.norm.Norm.Norm}
        """
        self.set = set
        self.membership = None
        self.COM = COM

    def setMembershipForValue(self,value):
        """Get membership for an input value from the fuzzy set."""
        self.membership = self.set(value)

    def getMembership(self):
        """Return membership set in this adjective."""
        if self.membership is None:
            return 0.0
        else:
            return self.membership

    def setMembership(self,value):
        """Set membership of this adjective as result 
           of a rule calculation, 
           if already set use COM norm to merge
           old and new value."""

        if self.membership is None:
            self.membership = value
        else:
            self.membership = (self.COM or self._COM)(
                                                    self.membership,  # consider already set value
                                                    value
                                                )

    def reset(self):
        """Reset membership to unknown value (None)."""
        self.membership = None

    def getName(self,system):
        """Find own name in given system.
        Returns a tuple (var_name,adj_name) of None."""
        return system.findAdjectiveName(self)
