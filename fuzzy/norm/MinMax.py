# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: MinMax.py,v 1.2 2008-10-08 13:11:39 rliebscher Exp $"

from fuzzy.norm.Norm import NormException
from fuzzy.norm.ParametricNorm import ParametricNorm

class MinMax(ParametricNorm):

    def __init__(self,p=0.5):
        ParametricNorm.__init__(self,0,p)

    def __call__(self,*args):
        if len(args) != 2:
            raise NormException("%s is supported only for 2 parameters" % self.__class__.__name__ )
        p = self.p
        x = float(args[0])
        y = float(args[1])
        return (1.0-p)*min(x,y)+p*max(x,y)
