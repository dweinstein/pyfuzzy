# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariable.py,v 1.7 2008-11-25 14:01:51 rliebscher Exp $"


from fuzzy.Variable import Variable


class OutputVariable(Variable):
    """General instance of an output variable.
        The defuzzification is provided by special object for this purpose,
        set as defuuzy param.
        Also marker, so you can check if any variable is an (instance of) output variable 

        @ivar defuzzy: Defuzzification method.
        @type defuzzy: L{fuzzy.defuzzy.Base.Base}
       """

    def __init__(self,defuzzy=None,*args,**keywords):
        """Initialize this output variable with a defuzzification method.
        
        @param defuzzy: Defuzzification method.
        @type defuzzy: L{fuzzy.defuzzy.Base.Base}
        """
        super(OutputVariable, self).__init__(*args,**keywords)
        self.defuzzy = defuzzy

    def getValue(self):
        """defuzzyfication"""
        return self.defuzzy.getValue(self)
