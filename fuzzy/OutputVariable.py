# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: OutputVariable.py,v 1.3 2008-10-08 13:19:17 rliebscher Exp $"


from fuzzy.Variable import Variable


class OutputVariable(Variable):
    """marker class, so you can check if any variable is an (instance of) output variable 
       """

    def __init__(self,*args,**keywords):
        Variable.__init__(*tuple([self]+list(args)),**keywords)
