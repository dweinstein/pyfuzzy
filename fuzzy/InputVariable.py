# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: InputVariable.py,v 1.3 2008-11-11 12:46:30 rliebscher Exp $"


from fuzzy.Variable import Variable


class InputVariable(Variable):
    """marker class, so you can check if any variable is an (instance of) input variable 
       """

    def __init__(self,*args,**keywords):
        super(InputVariable, self).__init__(*args,**keywords)
