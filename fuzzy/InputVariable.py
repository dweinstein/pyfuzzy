
__revision__ = "$Id: InputVariable.py,v 1.1 2003-04-21 10:59:32 plafoucr Exp $"


from fuzzy.Variable import Variable


class InputVariable(Variable):
    """marker class, so you can check if any variable is an (instance of) input variable 
       """

    def __init__(self,*args,**keywords):
        Variable.__init__(*tuple([self]+list(args)),**keywords)
