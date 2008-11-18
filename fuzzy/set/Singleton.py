# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Singleton.py,v 1.9 2008-11-18 21:46:48 rliebscher Exp $"


from fuzzy.set.Polygon import Polygon
from fuzzy.utils import prop

# use Polygon as base class so we dont need write all
# methods again
class Singleton(Polygon):
    """This set represents a non-fuzzy number.
    
    Its membership is only for x equal 1.::
    
              *
              |
              |
              |
         -----+-----
              x
    """

    def __init__(self,x=0.0):
        super(Singleton,self).__init__()
        self.x = x # update polygon

    @prop
    def x():
        """x
        @type: float"""
        def fget(self):
            return self._x
        def fset(self,value):
            self._x = value
            self._update()
        return locals()

    def _update(self):
        """update polygon"""
        p = super(Singleton, self)
        p.clear()
        p.add(self._x,0.0)
        p.add(self._x,1.0)
        p.add(self._x,0.0)

    def __call__(self,x):
        """Get membership of value x."""
        if x == self._x:
            return 1.0
        else:
            return 0.0

    def getCOG(self):
        """Return center of gravity."""
        return self._x

    def add(self,x,y,where=Polygon.END):
        """Don't let anyone destroy our singleton."""
        raise Exception()

    def remove(self,x,where=Polygon.END):
        """Don't let anyone destroy our singleton."""
        raise Exception()

    def clear(self):
        """Don't let anyone destroy our singleton."""
        raise Exception()

