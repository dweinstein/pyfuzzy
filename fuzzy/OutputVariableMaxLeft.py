# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariableMaxLeft.py,v 1.6 2008-11-11 12:46:30 rliebscher Exp $"


from fuzzy.OutputVariable import OutputVariable
from fuzzy.defuzzify.MaxLeft import MaxLeft


class OutputVariableMaxLeft(OutputVariable):
    """Output variable which uses for defuzzyfication
       the left maximum."""

    def __init__(self, INF=None, ACC=None, failsafe=None,*args,**keywords):
        defuzzy = MaxLeft(INF,ACC,failsafe)
        super(OutputVariableMaxLeft, self).__init__(defuzzy,*args,**keywords)
