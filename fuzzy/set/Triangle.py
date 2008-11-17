# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Triangle.py,v 1.10 2008-11-17 09:31:53 rliebscher Exp $"


from fuzzy.set.Polygon import Polygon

class Triangle(Polygon):
    """Triangle shaped fuzzy set."""

    def __init__(self,y_max=1.0,y_min=0.0,m=0.0,alpha=1.0,beta=1.0):
        r"""Constructor.
        y_max:  y-value at top of the triangle (1.0)
        y_min:  y-value outside the triangle (0.0)
        m:      x-value of top of triangle (0.0)
        alpha:  distance of left corner to m (1.0)
        beta:   distance of right corner to m (1.0)

             ______  y_max
             ^
            /|\
           / | \
          /  |  \
        _/   |   \_  y_min
         |   m   |
         |   |   |
        alpha|beta

        http://pyfuzzy.sourceforge.net/test/set/Triangle.png

        """
        super(Triangle, self).__init__()
        self._y_max = y_max
        self._y_min = y_min
        self._m = m
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
    def m():
        doc = """m"""
        def fget(self):
            return self._m
        def fset(self,value):
            self._m = value
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
        """update polygon"""
        p = super(Triangle, self)
        p.clear()
        p.add(self._m-self._alpha,self._y_min)
        p.add(self._m,self._y_max)
        p.add(self._m+self._beta,self._y_min)

    def add(self,x,y,where=Polygon.END):
        """Don't let anyone destroy our triangle."""
        raise Exception()

    def remove(self,x,where=Polygon.END):
        """Don't let anyone destroy our triangle."""
        raise Exception()

    def clear(self):
        """Don't let anyone destroy our triangle."""
        raise Exception()

