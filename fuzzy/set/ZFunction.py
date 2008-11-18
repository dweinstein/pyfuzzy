# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: ZFunction.py,v 1.11 2008-11-18 18:55:06 rliebscher Exp $"


from fuzzy.set.SFunction import SFunction

class ZFunction(SFunction):
    """Z shaped fuzzy set."""

    def __init__(self,a=0.0,delta=1.0):
        r"""
        Realize a Z-shaped fuzzy set::
           __
             \
             |\
             | \
             | |\
             | | \__
             | a |
             |   |
             delta

        see also U{http://pyfuzzy.sourceforge.net/test/set/ZFunction.png}

        @param a: center of set
        @type a: float
        @param delta: absolute distance between x-values for minimum and maximum
        @type delta: float
        """
        super(ZFunction, self).__init__(a,delta)


    def __call__(self,x):
        """Return membership of x in this fuzzy set.
           This method makes the set work like a function.
           
           @param x: value for which the membership is to calculate
           @type x: float
           @return: membership
           @rtype: float
           """
        return 1.0 - SFunction.__call__(self,x)

