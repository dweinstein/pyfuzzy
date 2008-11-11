# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariable.py,v 1.4 2008-11-11 12:46:30 rliebscher Exp $"


from fuzzy.Variable import Variable


class OutputVariable(Variable):
    """marker class, so you can check if any variable is an (instance of) output variable 
       """

    def __init__(self,defuzzy=None,*args,**keywords):
        super(OutputVariable, self).__init__(*args,**keywords)
        self.defuzzy = defuzzy
    
    def getValue(self):
        """defuzzyfication"""
        return self.defuzzy.getValue(self)
