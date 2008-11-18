# -*- coding: iso-8859-1 -*-
""" 
    Base class for any kind of parametric fuzzy norm.
"""

__revision__ = "$Id: ParametricNorm.py,v 1.5 2008-11-18 21:46:48 rliebscher Exp $"

from fuzzy.norm.Norm import Norm

class ParametricNorm(Norm):
    """Abstract base class for any parametric fuzzy norm
    
    @ivar p: parameter for norm
    @type p: float
    """

    def __init__(self,type=0,p=0.5):
        """Initialize type and parameter
        
        @param p: parameter for norm
        @type p: float
        """
        super(ParametricNorm,self).__init__(type)
        self.p = p
