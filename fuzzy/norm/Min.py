# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Min.py,v 1.3 2008-10-08 13:11:39 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class Min(Norm):

    def __init__(self):
        Norm.__init__(self,Norm.T_NORM)

    def __call__(self,*args):
	"""Return minimum of given values."""
        return min(args)
