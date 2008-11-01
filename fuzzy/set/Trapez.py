# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Trapez.py,v 1.6 2008-11-01 13:19:23 rliebscher Exp $"


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
        Polygon.__init__(self)
        # don't trigger __setattr__
        self.__dict__["y_max"] = y_max
        self.__dict__["y_min"] = y_min
        self.__dict__["m1"] = m1
        self.__dict__["m2"] = m2
        self.__dict__["alpha"] = alpha
        self.beta = beta # update polygon

    def __setattr__(self,name,value):
        self.__dict__[name] = value
        if name in ["y_max",
                    "y_min",
                    "m1",
                    "m2",
                    "alpha",
                    "beta"]:
            # update polygon
            Polygon.clear(self)
            Polygon.add(self,self.m1-self.alpha,self.y_min)
            Polygon.add(self,self.m1,self.y_max)
            Polygon.add(self,self.m2,self.y_max)
            Polygon.add(self,self.m2+self.beta,self.y_min)

    def add(self,x,y,where=Polygon.END):
        """Don't let anyone destroy our trapez."""
        raise Exception()

    def remove(self,x,where=Polygon.END):
        """Don't let anyone destroy our trapez."""
        raise Exception()

    def clear(self):
        """Don't let anyone destroy our trapez."""
        raise Exception()

