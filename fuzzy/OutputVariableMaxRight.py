# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariableMaxRight.py,v 1.6 2008-11-11 12:46:30 rliebscher Exp $"


from fuzzy.OutputVariable import OutputVariable
from fuzzy.defuzzify.MaxRight import MaxRight

class OutputVariableMaxRight(OutputVariable):
    """Output variable which uses for defuzzyfication
       the right maximum."""

    def __init__(self, INF=None, ACC=None, failsafe=None,*args,**keywords):
        defuzzy = MaxRight(INF,ACC,failsafe)
        super(OutputVariableMaxRight,self).__init__(defuzzy,*args,**keywords)
