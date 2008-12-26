# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: HarmonicMean.py,v 1.4 2008-12-26 17:51:33 rliebscher Exp $"

from fuzzy.norm.Norm import Norm,sum

class HarmonicMean(Norm):

    def __init__(self):
        Norm.__init__(self,0)

    def __call__(self,*args):
        if 0. in args:
            return 0.
        return float(len(args))/sum(*[1.0/x for x in args])
