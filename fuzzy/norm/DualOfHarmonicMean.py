# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: DualOfHarmonicMean.py,v 1.3 2008-12-26 17:51:33 rliebscher Exp $"

from fuzzy.norm.Norm import Norm,product,sum

class DualOfHarmonicMean(Norm):

    def __init__(self):
        Norm.__init__(self,0) #XXX

    def __call__(self,*args):
        sum_ = sum(*args)
        if sum_ == len(args): return 1.0
        product_ = product(*args)
        count_ = float(len(args))
        return (sum_-count_*product_)/(count_-sum_) 
