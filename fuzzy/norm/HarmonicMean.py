# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: HarmonicMean.py,v 1.3 2008-11-01 13:13:52 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class HarmonicMean(Norm):

    def __init__(self):
        Norm.__init__(self,0)

    def __call__(self,*args):
        if 0. in args:
            return 0.
        return float(len(args))/reduce(lambda x,y:x+y,[1.0/x for x in args])
