# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: GammaOperator.py,v 1.3 2008-11-01 13:13:52 rliebscher Exp $"

from fuzzy.norm.Norm import NormException
from fuzzy.norm.ParametricNorm import ParametricNorm

class GammaOperator(ParametricNorm):

    def __init__(self,p=0.5):
        ParametricNorm.__init__(self,0,p)

    def __call__(self,*args):
        if len(args) != 2:
            raise NormException("%s is supported only for 2 parameters" % self.__class__.__name__ )
        p = self.p
        x = float(args[0])
        y = float(args[1])
        if x == 0. or y == 0.:
            return 0.
        return x*y*pow((x+y)/(x*y)-1,p)
