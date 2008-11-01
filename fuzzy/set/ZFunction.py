# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: ZFunction.py,v 1.8 2008-11-01 13:19:23 rliebscher Exp $"


from fuzzy.set.SFunction import SFunction

class ZFunction(SFunction):
    """Z shaped fuzzy set."""

    def __init__(self,a=0.0,delta=1.0):
        """
           __
             \
             |\
             | \
             | |\
             | | \__
             | a |
             |   |
             delta

        http://pyfuzzy.sourceforge.net/test/set/ZFunction.png

        """
        SFunction.__init__(self,a,delta)


    def __call__(self,x):
        """Return membership of x in this fuzzy set.
           This method makes the set work like a function."""
        return 1.0 - SFunction.__call__(self,x)

