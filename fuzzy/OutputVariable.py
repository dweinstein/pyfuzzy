# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariable.py,v 1.8 2009-01-09 22:01:35 rliebscher Exp $"


from fuzzy.Variable import Variable


class OutputVariable(Variable):
    """General instance of an output variable.
        The defuzzification is provided by special object for this purpose,
        set as defuzzify param.
        Also marker, so you can check if any variable is an (instance of) output variable 

        @ivar defuzzify: Defuzzification method.
        @type defuzzify: L{fuzzy.defuzzify.Base.Base}
       """

    def __init__(self,defuzzify=None,*args,**keywords):
        """Initialize this output variable with a defuzzification method.

        @param defuzzify: Defuzzification method.
        @type defuzzify: L{fuzzy.defuzzify.Base.Base}
        """
        super(OutputVariable, self).__init__(*args,**keywords)
        self.defuzzify = defuzzify

    def getValue(self):
        """defuzzyfication"""
        return self.defuzzify.getValue(self)
