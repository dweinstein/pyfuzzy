
__revision__ = "$Id: OutputVariable.py,v 1.2 2003-06-11 13:29:11 rliebscher Exp $"


from fuzzy.Variable import Variable


class OutputVariable(Variable):
    """marker class, so you can check if any variable is an (instance of) output variable 
       """

    def __init__(self,*args,**keywords):
        Variable.__init__(*tuple([self]+list(args)),**keywords)
