# -*- coding: iso-8859-1 -*-
""" 
    Abstract base class for any kind of fuzzy norm.
"""

__revision__ = "$Id: Norm.py,v 1.6 2008-11-12 21:53:40 rliebscher Exp $"

from fuzzy.Exception import Exception
class NormException(Exception):
    pass


class Norm(object):

    T_NORM = 1
    S_NORM = 2

    def __init__(self,type=0):
        self.__type = type

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
        return self.__type
