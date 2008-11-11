# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: MaxRight.py,v 1.1 2008-11-11 12:50:02 rliebscher Exp $"

from fuzzy.defuzzify.Base import Base

class MaxRight(Base):
    """Defuzzyfication which uses the right maximum."""

    def __init__(self, INF=None, ACC=None, failsafe=None,*args,**keywords):
        super(MaxRight, self).__init__(INF,ACC,*args,**keywords)
        self.failsafe = failsafe # which value if value not calculable

    def getValue(self,variable):
        """Defuzzyfication."""
        try:
            temp = self.accumulate(variable)

            # get polygon representation
            table = list(self.value_table(temp))
            table.reverse()
            #print table

            y = table[0][1]
            x = float('+inf') # right end of polygon is always infinity

            for (x_,y_) in table[1:]:        
                if y_ > y:
                    y = y_
                    x = x_

            return x
        except:
            # was not to calculate
            if self.failsafe is not None:
                # user gave us a value to return
                return self.failsafe
            else:
                raise
