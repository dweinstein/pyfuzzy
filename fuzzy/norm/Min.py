# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Min.py,v 1.4 2008-10-24 20:47:09 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class Min(Norm):

    def __init__(self):
        Norm.__init__(self,Norm.T_NORM)

    def __call__(self,*args):
        """Return minimum of given values."""
        return min(args)
