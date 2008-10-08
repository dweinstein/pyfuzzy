# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: InputVariable.py,v 1.2 2008-10-08 13:19:17 rliebscher Exp $"


from fuzzy.Variable import Variable


class InputVariable(Variable):
    """marker class, so you can check if any variable is an (instance of) input variable 
       """

    def __init__(self,*args,**keywords):
        Variable.__init__(*tuple([self]+list(args)),**keywords)
