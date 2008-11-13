# -*- coding: iso-8859-1 -*-
""" 
    Abstract base class for any kind of fuzzy norm.
"""

__revision__ = "$Id: Norm.py,v 1.7 2008-11-13 20:45:17 rliebscher Exp $"

from fuzzy.Exception import Exception
class NormException(Exception):
    pass


class Norm(object):
    """Abstract Base class of any fuzzy norm"""

    # types of norm
    UNKNOWN = 0
    T_NORM = 1
    S_NORM = 2

    def __init__(self,type=0):
        """Initialize type of norm"""
        self._type = type

    def __call__(self,*args):
        """
            Calculate result of norm(arg1,arg2,...)
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
