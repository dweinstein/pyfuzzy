# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: DualOfGeometricMean.py,v 1.2 2008-10-08 13:11:39 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class DualOfGeometricMean(Norm):

    def __init__(self):
        Norm.__init__(self,0) # XXX

    def __call__(self,*args):
        return 1.0 - pow(reduce(lambda x,y:x*y,
                                map(lambda x:1.0-x,
                                    args
                                   )    
                               ),1.0/len(args)) 
