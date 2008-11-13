# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Adjective.py,v 1.9 2008-11-13 20:45:17 rliebscher Exp $"


from fuzzy.norm.Max import Max
from fuzzy.set.Set import Set

class Adjective(object):
    """Describes a ... of a variable."""

    # default if not set in instance
    _COM = Max()

    def __init__(self,set=Set(),COM=None):
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
