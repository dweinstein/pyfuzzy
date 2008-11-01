# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: HamacherSum.py,v 1.3 2008-11-01 13:13:52 rliebscher Exp $"

from fuzzy.norm.Norm import Norm,NormException

class HamacherSum(Norm):

    def __init__(self):
        Norm.__init__(self,Norm.S_NORM)

    def __call__(self,*args):
        if len(args) != 2:
            raise NormException("%s is supported only for 2 parameters" % self.__class__.__name__ )
        x = float(args[0])
        y = float(args[1])
        if x*y == 1.:
            return 1.
        return (x+y-2.0*x*y)/(1.0-x*y)