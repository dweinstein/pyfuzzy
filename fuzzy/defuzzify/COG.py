# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: COG.py,v 1.2 2008-11-18 18:55:06 rliebscher Exp $"

from fuzzy.defuzzify.Base import Base

class COG(Base):
    """defuzzification which uses
       the center of gravity method."""

    def __init__(self, INF=None, ACC=None, failsafe=None,*args,**keywords):
        """
            @param failsafe: if is not possible to calculate a center of gravity,
            return this value if not None or forward the exception
        """ 
        super(COG, self).__init__(INF,ACC,*args,**keywords)
        self.failsafe = failsafe # which value if COG not calculable

    def getValue(self,variable):
        """Defuzzyfication using center of gravity method."""
        temp = self.accumulate(variable)
        try:
            return temp.getCOG()
        except:
            # was not to calculate
            if self.failsafe is not None:
                # user gave us a value to return
                return self.failsafe
            else:
                # forward exception
                raise
