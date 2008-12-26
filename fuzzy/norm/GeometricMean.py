# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: GeometricMean.py,v 1.3 2008-12-26 17:51:33 rliebscher Exp $"

from fuzzy.norm.Norm import Norm,product

class GeometricMean(Norm):

    def __init__(self):
        Norm.__init__(self,0)

    def __call__(self,*args):
        return pow(product(*args),1.0/len(args)) 
