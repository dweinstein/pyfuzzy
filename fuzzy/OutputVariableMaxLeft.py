# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariableMaxLeft.py,v 1.7 2008-11-18 18:55:06 rliebscher Exp $"


from fuzzy.OutputVariable import OutputVariable
from fuzzy.defuzzify.MaxLeft import MaxLeft


class OutputVariableMaxLeft(OutputVariable):
    """Output variable which uses for defuzzyfication
       the left maximum.
       
       @deprecated: set defuzzy of OutputVariable
    """

    def __init__(self, INF=None, ACC=None, failsafe=None,*args,**keywords):
        defuzzy = MaxLeft(INF,ACC,failsafe)
        super(OutputVariableMaxLeft, self).__init__(defuzzy,*args,**keywords)
