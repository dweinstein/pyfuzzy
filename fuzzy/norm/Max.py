# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Max.py,v 1.4 2008-10-24 20:47:09 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class Max(Norm):

    def __init__(self):
        Norm.__init__(self,Norm.S_NORM)

    def __call__(self,*args):
        """Return maximum of given values."""
        return max(args)
