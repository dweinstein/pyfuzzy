# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: COG.py,v 1.4 2009-01-09 22:01:35 rliebscher Exp $"

from fuzzy.defuzzify.Base import Base

class COG(Base):
    """defuzzification which uses
       the center of gravity method."""

    def __init__(self, INF=None, ACC=None, failsafe=None, segment_size=None,*args,**keywords):
        """
            @param failsafe: if is not possible to calculate a center of gravity,
                             return this value if not None or forward the exception
            @param segment_size: maximum length of segment in polygon of accumulated result set
        """ 
        super(COG, self).__init__(INF,ACC,*args,**keywords)
        self.failsafe = failsafe # which value if COG not calculable
        self.segment_size = segment_size # maximum length of segment in polygon of accumulated result set

    def getValue(self,variable):
        """Defuzzyfication using center of gravity method."""
        temp = self.accumulate(variable,self.segment_size)
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
