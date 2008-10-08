# -*- coding: iso-8859-1 -*-
""" 
    Base class for any kind of parametric fuzzy norm.
"""

__revision__ = "$Id: ParametricNorm.py,v 1.2 2008-10-08 13:11:39 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class ParametricNorm(Norm):

    def __init__(self,type=0,p=0.5):
        Norm.__init__(self,type)
        self.p = p
    