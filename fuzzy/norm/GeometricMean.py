# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: GeometricMean.py,v 1.2 2008-10-08 13:11:39 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class GeometricMean(Norm):

    def __init__(self):
        Norm.__init__(self,0)

    def __call__(self,*args):
        return pow(reduce(lambda x,y:x*y,args),1.0/len(args)) 
