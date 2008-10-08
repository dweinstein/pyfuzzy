# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: System.py,v 1.4 2008-10-08 13:19:17 rliebscher Exp $"


class System:
    """Holds all stuff together. (variables, rules, ...)
       Provides methods to do calculation with it.""" 
    
    def __init__(self):
	"""Constructor.
	Creates two instance variables:
	variables: dictionary to hold all variables.
	rules:	   dictionary to hold all rules.
	"""
        self.variables = {}
        self.rules = {}

    def calculate(self,input,output):
        """Do a complete fuzzy calculation step.
        The input dictionary contains the input values for the named variables.
        The output dictionary serves as container and provides the names of the
        variables to read."""
        
        # reset everything what might be left from last run
        for variable in self.variables.values():
            variable.reset()

        # feed input values in variables and so in adjectives
        for (name,value) in input.items():
            self.variables[name].setValue(value)

        # compute fuzzy rules 
        for rule in self.rules.values():
            rule.compute()

        # get all wanted output variables    
        for name in output.keys():
            output[name] = self.variables[name].getValue()

        return output

    def findVariableName(self,var):
        for name,variable in self.variables.iteritems():
	    if var is variable:
		return name
	return None
		
    def findAdjectiveName(self,adj):
        for name,variable in self.variables.iteritems():
    	    for namea,adjective in variable.adjectives.iteritems():
		if adj is adjective:
		    return [namea,name]
	return None
	