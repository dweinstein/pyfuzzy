# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: InputVariable.py,v 1.4 2009-01-09 22:01:35 rliebscher Exp $"


from fuzzy.Variable import Variable


class InputVariable(Variable):
    """General instance of an input variable 
        The fuzzification is provided by special object for this purpose,
        set as fuzzify param.
        Also marker, so you can check if any variable is an (instance of) input variable 

        @ivar fuzzify: Fuzzification method.
        @type fuzzify: L{fuzzy.fuzzify.Base.Base}
       """

    def __init__(self,fuzzify=None,*args,**keywords):
        """Initialize this input variable with a fuzzification method.

        @param fuzzify: Fuzzification method.
        @type fuzzify: L{fuzzy.fuzzify.Base.Base}
        """
        super(InputVariable, self).__init__(*args,**keywords)
        self.fuzzify = fuzzify

    def setValue(self,value):
        """Let adjectives calculate their membership values."""
        self.__value = self.fuzzify.setValue(self,value)

