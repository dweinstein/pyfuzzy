# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Trapez.py,v 1.10 2008-11-18 18:55:06 rliebscher Exp $"


from fuzzy.set.Polygon import Polygon
from fuzzy.utils import prop

class Trapez(Polygon):

    def __init__(self,y_max=1.0,y_min=0.0,m1=-0.5,m2=0.5,alpha=0.5,beta=0.5):
        r"""
        Realize a Trapez-shaped fuzzy set::
               _____ _____  y_max
              /     \
             /|     |\
            / |     | \
           /  |     |  \
         _/   |     |   \_  y_min
          |   m1    m2  |
          |   |     |   |
         alpha|     |beta

        See also U{http://pyfuzzy.sourceforge.net/test/set/Trapez.png}

        @param y_max:  y-value at top of the trapez (1.0)
        @param y_min:  y-value outside the trapez (0.0)
        @param m1:     x-value of left top of trapez (-0.5)
        @param m2:     x-value of right top of trapez (0.5)
        @param alpha:  distance of left corner to m1 (0.5)
        @param beta:   distance of right corner to m2 (0.5)
        """
        super(Trapez, self).__init__()
        self._y_max = y_max
        self._y_min = y_min
        self._m1 = m1
        self._m2 = m2
        self._alpha = alpha
        self._beta = beta
        self._update() # update polygon

    @prop
    def y_max():
        """y_max"""
        def fget(self):
            return self._y_max
        def fset(self,value):
            self._y_max = value
            self._update()
        return locals()

    @prop
    def y_min():
        """y_min"""
        def fget(self):
            return self._y_min
        def fset(self,value):
            self._y_min = value
            self._update()
        return locals()

    @prop
    def m1():
        """m1"""
        def fget(self):
            return self._m1
        def fset(self,value):
            self._m1 = value
            self._update()
        return locals()

    @prop
    def m2():
        """m2"""
        def fget(self):
            return self._m2
        def fset(self,value):
            self._m2 = value
            self._update()
        return locals()

    @prop
    def alpha():
        """alpha"""
        def fget(self):
            return self._alpha
        def fset(self,value):
            self._alpha = value
            self._update()
        return locals()

    @prop
    def beta():
        """beta"""
        def fget(self):
            return self._beta
        def fset(self,value):
            self._beta = value
            self._update()
        return locals()

    def _update(self):
        """update polygon"""
        p = super(Trapez, self)
        p.clear()
        p.add(self._m1-self._alpha,self._y_min)
        p.add(self._m1,self._y_max)
        p.add(self._m2,self._y_max)
        p.add(self._m2+self._beta,self._y_min)

    def add(self,x,y,where=Polygon.END):
        """Don't let anyone destroy our trapez."""
        raise Exception()

    def remove(self,x,where=Polygon.END):
        """Don't let anyone destroy our trapez."""
        raise Exception()

    def clear(self):
        """Don't let anyone destroy our trapez."""
        raise Exception()

