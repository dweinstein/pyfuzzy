""" 
    Base class for any kind of parametric fuzzy norm.
"""
from fuzzy.norm.Norm import Norm

class ParametricNorm(Norm):

    def __init__(self,type=0,p=0.5):
        Norm.__init__(self,type)
        self.p = p
    