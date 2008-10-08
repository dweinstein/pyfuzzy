# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: SchweizerIntersection.py,v 1.2 2008-10-08 13:11:39 rliebscher Exp $"

from fuzzy.norm.Norm import NormException
from fuzzy.norm.ParametricNorm import ParametricNorm

class SchweizerIntersection(ParametricNorm):

    def __init__(self,p=0.5):
        ParametricNorm.__init__(self,ParametricNorm.T_NORM,p)

    def __call__(self,*args):
        if len(args) != 2:
            raise NormException("%s is supported only for 2 parameters" % self.__class__.__name__ )
        p = self.p
        x = float(args[0])
        y = float(args[1])
        return pow(max(0.0,pow(x,p)+pow(y,p)-1.0),1.0/p)