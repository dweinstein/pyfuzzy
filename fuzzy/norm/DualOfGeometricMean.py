# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: DualOfGeometricMean.py,v 1.5 2008-12-26 17:51:33 rliebscher Exp $"

from fuzzy.norm.Norm import Norm,product

class DualOfGeometricMean(Norm):

    def __init__(self):
        Norm.__init__(self,0) # XXX

    def __call__(self,*args):
        return 1.0 - pow(product(*[1.0-x for x in args]),1.0/len(args)) 
