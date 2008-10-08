# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Max.py,v 1.3 2008-10-08 13:11:39 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class Max(Norm):

    def __init__(self):
        Norm.__init__(self,Norm.S_NORM)

    def __call__(self,*args):
	"""Return maximum of given values."""
        return max(args)
