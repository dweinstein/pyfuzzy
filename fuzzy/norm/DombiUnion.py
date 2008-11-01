# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: DombiUnion.py,v 1.3 2008-11-01 13:13:52 rliebscher Exp $"

from fuzzy.norm.Norm import NormException
from fuzzy.norm.ParametricNorm import ParametricNorm

class DombiUnion(ParametricNorm):

    def __init__(self,p=0.5):
        ParametricNorm.__init__(self,ParametricNorm.S_NORM,p)

    def __call__(self,*args):
        if len(args) != 2:
            raise NormException("%s is supported only for 2 parameters" % self.__class__.__name__ )
        p = self.p
        x = float(args[0])
        y = float(args[1])
        if x == 1. or y == 1.:
            return 1.
        def f(x,p):
            return pow(x/(1.0-x),p)
        return 1.0-1.0/(1.0+pow(f(x,p)+f(y,p),1.0/p))