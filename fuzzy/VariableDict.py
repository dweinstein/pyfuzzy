from fuzzy.Variable import Variable

class VariableDict(Variable):
    """Given values not as number, instead give an dictionary of memberships."""

    def __init__(self,*args,**keywords):
        Variable.__init__(*tuple([self]+list(args)),**keywords)
        
    def setValue(self,value):
        """Set adjectives to their membership values."""
        self.__value = value
        for adjective in value.keys():
            self.adjectives[adjective].setMembership(value[adjective])
	# what want we to do if values contain adjective names we don't have?
	# currently this gives a KeyError
