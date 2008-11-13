# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariable.py,v 1.5 2008-11-13 20:45:17 rliebscher Exp $"


from fuzzy.Variable import Variable


class OutputVariable(Variable):
    """General instance of an output variable.
        The defuzzification is provided by special object for this purpose,
        set as defuuzy param.
        Also marker, so you can check if any variable is an (instance of) output variable 
       """

    def __init__(self,defuzzy=None,*args,**keywords):
        """Initialize this output variable with a defuzzification method."""
        super(OutputVariable, self).__init__(*args,**keywords)
        self.defuzzy = defuzzy

    def getValue(self):
        """defuzzyfication"""
        return self.defuzzy.getValue(self)
