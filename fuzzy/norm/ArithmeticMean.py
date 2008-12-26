# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: ArithmeticMean.py,v 1.3 2008-12-26 17:51:33 rliebscher Exp $"

from fuzzy.norm.Norm import Norm,sum

class ArithmeticMean(Norm):

    def __init__(self):
        Norm.__init__(self,0)

    def __call__(self,*args):
        return sum(*args)/float(len(args))
