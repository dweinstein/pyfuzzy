# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: LM.py,v 1.1 2008-12-26 17:56:13 rliebscher Exp $"

from fuzzy.defuzzify.Base import Base,DefuzzificationException

class LM(Base):
    """Defuzzyfication which uses the left most (local) maximum."""

    def __init__(self, INF=None, ACC=None, failsafe=None,*args,**keywords):
        """Initialize the defuzzification method with INF,ACC 
        and an optional value in case defuzzification is not possible"""
        super(LM, self).__init__(INF,ACC,*args,**keywords)
        self.failsafe = failsafe # which value if value not calculable

    def getValue(self,variable):
        """Defuzzyfication."""
        try:
            temp = self.accumulate(variable)

            # get polygon representation
            table = list(self.value_table(temp))

            if len(table) == 0:
                raise DefuzzificationException("no value calculable: complete undefined set")

            y = table[0][1]
            x = float('-inf') # left end of polygon is always -infinity

            for (x_,y_) in table[1:]:
                if y_ > y:
                    y = y_
                    x = x_
                else:
                    break

            return x
        except:
            # was not to calculate
            if self.failsafe is not None:
                # user gave us a value to return
                return self.failsafe
            else:
                raise
