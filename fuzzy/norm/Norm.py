""" 
    Abstract base class for any kind of fuzzy norm.
"""
from fuzzy.Exception import Exception
class NormException(Exception):
    pass


class Norm:

    T_NORM = 1
    S_NORM = 2

    def __init__(self,type=0):
        self.__type = type
        
    def __call__(self,*args):
        raise NormException("abstract class %s can't be called" % self.__class__.__name__)
        
    def getType(self):
        return self.__type
    