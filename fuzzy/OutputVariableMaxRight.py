# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariableMaxRight.py,v 1.7 2008-11-18 18:55:06 rliebscher Exp $"


from fuzzy.OutputVariable import OutputVariable
from fuzzy.defuzzify.MaxRight import MaxRight

class OutputVariableMaxRight(OutputVariable):
    """Output variable which uses for defuzzyfication
       the right maximum.
       
       @deprecated: set defuzzy of OutputVariable
    """

    def __init__(self, INF=None, ACC=None, failsafe=None,*args,**keywords):
        defuzzy = MaxRight(INF,ACC,failsafe)
        super(OutputVariableMaxRight,self).__init__(defuzzy,*args,**keywords)
