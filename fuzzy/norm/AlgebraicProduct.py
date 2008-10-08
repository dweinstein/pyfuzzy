# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: AlgebraicProduct.py,v 1.2 2008-10-08 13:11:39 rliebscher Exp $"

from fuzzy.norm.Norm import Norm,NormException

class AlgebraicProduct(Norm):

    def __init__(self):
        Norm.__init__(self,Norm.T_NORM)

    def __call__(self,*args):
        if len(args) != 2:
            raise NormException("%s is supported only for 2 parameters" % self.__class__.__name__ )
        x = float(args[0])
        y = float(args[1])
        return x*y