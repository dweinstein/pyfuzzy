# -*- coding: iso-8859-1 -*-
""" 
    Base class for any kind of parametric fuzzy norm.
"""

__revision__ = "$Id: ParametricNorm.py,v 1.4 2008-11-13 20:45:17 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class ParametricNorm(Norm):
    """Abstract base class for any parametric fuzzy norm"""

    def __init__(self,type=0,p=0.5):
        """Initialize type and parameter"""
        super(ParametricNorm,self).__init__(type)
        self.p = p
