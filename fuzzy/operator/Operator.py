# -*- coding: iso-8859-1 -*-
"""
    Calculate value for fuzzy rule.
    
    Used to build fuzzy rules.
""" 

__revision__ = "$Id: Operator.py,v 1.5 2008-10-24 20:47:09 rliebscher Exp $"


import fuzzy.Exception

class Operator:
    """Abstract base class for any kind of operator."""

    def __init__(self):
        """Dummy initialization, so it is safe to call it
           from any sub class."""  
        pass
 
    def __call__(self):
        """Return current value."""
        raise fuzzy.Exception.Exception("abtract class %s can't be called" % self.__class__.__name__)

    def printDot(self,system,parent_name):
        raise fuzzy.Exception.Exception("abtract class %s can't be called" % self.__class__.__name__)
