# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: ArithmeticMean.py,v 1.2 2008-10-08 13:11:39 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class ArithmeticMean(Norm):

    def __init__(self):
        Norm.__init__(self,0)

    def __call__(self,*args):
        return reduce(lambda x,y:x+y,args)/float(len(args)) 
