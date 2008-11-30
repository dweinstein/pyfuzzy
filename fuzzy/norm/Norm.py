# -*- coding: iso-8859-1 -*-
""" 
    Abstract base class for any kind of fuzzy norm.
"""

__revision__ = "$Id: Norm.py,v 1.9 2008-11-30 20:22:23 rliebscher Exp $"

from fuzzy.Exception import Exception
class NormException(Exception):
    """Base class for any exception in norm calculations."""
    pass


class Norm(object):
    """Abstract Base class of any fuzzy norm"""

    # types of norm
    UNKNOWN = 0 #: type of norm unknown
    T_NORM = 1 #: norm is t-norm
    S_NORM = 2 #: norm is s-norm

    def __init__(self,type=0):
        """Initialize type of norm"""
        self._type = type

    def __call__(self,*args):
        """
            Calculate result of norm(arg1,arg2,...)
        
            @param args: list of floats as arguments for norm.
            @type args: list of float
            @return: result of norm calulation
            @rtype: float
            @raise NormException: any problem in calculation (wrong number of arguments, numerical problems)
        """
        raise NormException("abstract class %s can't be called" % self.__class__.__name__)

    def getType(self):
        """
            Return type of norm:
            0 = not defined or not classified
            1 = t-norm ( = Norm.T_NORM)
            2 = s-norm ( = Norm.S_NORM)

        """
        return self._type
