# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariableCOG.py,v 1.10 2008-11-18 18:55:06 rliebscher Exp $"


from fuzzy.OutputVariable import OutputVariable
from fuzzy.defuzzify.COG import COG

class OutputVariableCOG(OutputVariable):
    """Output variable which uses for defuzzyfication
       the center of gravity method.
       
       @deprecated: set defuzzy of OutputVariable
       """

    def __init__(self, INF=None, ACC=None, failsafe=None,*args,**keywords):
        """
            @param INF: inference norm, used with set of adjective and given value for it
            @param ACC: norm for accumulation of set of adjectives
            @param failsafe: if is not possible to calculate a center of gravity,
            return this value if not None or forward the exception
        """ 
        defuzzy = COG(INF,ACC,failsafe)
        super(OutputVariableCOG, self).__init__(defuzzy,*args,**keywords)
