# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Trapez.py,v 1.7 2008-11-11 12:17:20 rliebscher Exp $"


from fuzzy.set.Polygon import Polygon

class Trapez(Polygon):

    def __init__(self,y_max=1.0,y_min=0.0,m1=-0.5,m2=0.5,alpha=0.5,beta=0.5):
        """Constructor.
        y_max:  y-value at top of the trapez (1.0)
        y_min:  y-value outside the trapez (0.0)
        m1:     x-value of left top of trapez (-0.5)
        m2:     x-value of right top of trapez (0.5)
        alpha:  distance of left corner to m1 (0.5)
        beta:   distance of right corner to m2 (0.5)

              _____ _____  y_max
             /     \
            /|     |\
           / |     | \
          /  |     |  \
        _/   |     |   \_  y_min
         |   m1    m2  |
         |   |     |   |
        alpha|     |beta

        http://pyfuzzy.sourceforge.net/test/set/Trapez.png

        """
        super(Trapez, self).__init__()
        self._y_max = y_max
        self._y_min = y_min
        self._m1 = m1
        self._m2 = m2
        self._alpha = alpha
        self._beta = beta
        self._update() # update polygon

    @apply
    def y_max():
        doc = """y_max"""
        def fget(self):
            return self._y_max
        def fset(self,value):
            self._y_max = value
            self._update()
        return property(**locals())

    @apply
    def y_min():
        doc = """y_min"""
        def fget(self):
            return self._y_min
        def fset(self,value):
            self._y_min = value
            self._update()
        return property(**locals())

    @apply
    def m1():
        doc = """m1"""
        def fget(self):
            return self._m1
        def fset(self,value):
            self._m1 = value
            self._update()
        return property(**locals())

    @apply
    def m2():
        doc = """m2"""
        def fget(self):
            return self._m2
        def fset(self,value):
            self._m2 = value
            self._update()
        return property(**locals())

    @apply
    def alpha():
        doc = """alpha"""
        def fget(self):
            return self._alpha
        def fset(self,value):
            self._alpha = value
            self._update()
        return property(**locals())

    @apply
    def beta():
        doc = """beta"""
        def fget(self):
            return self._beta
        def fset(self,value):
            self._beta = value
            self._update()
        return property(**locals())

    def _update(self):
        # update polygon
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

