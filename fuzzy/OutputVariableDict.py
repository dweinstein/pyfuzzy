# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariableDict.py,v 1.7 2008-11-11 12:46:30 rliebscher Exp $"


from fuzzy.OutputVariable import OutputVariable
from fuzzy.defuzzify.Dict import Dict


class OutputVariableDict(OutputVariable):
    """Output variable which stores it adjective memberships
       in a dictionary for output.
       You should use in the adjectives instances of Set itself.
       
       What can be done with this?
       
       For example:
       You want help with buying a car.
       
       Input are your preferences:
       speed, payload (1-10), ...
       (map to "very important, important, doesn't matter, not wanted, never" ;-)
       
       Output are choices:
       cars with adjectives: ferrari, truck, ...
       
       rules are as follows:
       if speed->very_important && payload->never then car->ferrari
       if payload->very_important then car->truck
       ... and so on
       
       Then you use this as follows 
       input variables 
       { speed:3, payload:1, ...} 
       ==> 
       output_variables
       { car: {
                ferrari:0.1,
                truck: 1.0,
                ...
              }
       }

       """

    def __init__(self,*args,**keywords):
        super(OutputVariableDict, self).__init__(Dict(),*args,**keywords)
