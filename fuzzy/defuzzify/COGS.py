# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: COGS.py,v 1.2 2008-11-30 20:54:40 rliebscher Exp $"

from fuzzy.defuzzify.Base import Base
import fuzzy.set.Singleton

class COGS(Base):
    """defuzzification for singletons."""

    def __init__(self, INF=None, ACC=None, failsafe=None,*args,**keywords):
        """
            @param failsafe: if is not possible to calculate a center of gravity,
            return this value if not None or forward the exception
        """
        super(COGS, self).__init__(INF,ACC,*args,**keywords)
        self.failsafe = failsafe # which value if COG not calculable

    def getValue(self,variable):
        """Defuzzyfication using center of gravity method."""
        sum_1,sum_2 = 0.,0.
        for adjective in variable.adjectives.values():
            # get precomputed adjective set
            set = adjective.set
            if not isinstance(set,fuzzy.set.Singleton.Singleton):
                raise DefuzzificationException("Only Singleton for COGS defuzzification allowed.")
            a = (self.INF or self._INF)(set(set.x),adjective.getMembership())
            sum_1 += set.x*a
            sum_2 += a
        try:
            if sum_2 == 0.:
                raise DefuzzificationException("No result, all singletons set to 0.")
            return sum_1/sum_2
        except:
            # was not to calculate
            if self.failsafe is not None:
                # user gave us a value to return
                return self.failsafe
            else:
                # forward exception
                raise
