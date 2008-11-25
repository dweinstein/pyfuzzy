# -*- coding: iso-8859-1 -*-
""" """

__revision__ = "$Id: System.py,v 1.12 2008-11-25 14:01:51 rliebscher Exp $"


class System(object):
    """Holds all stuff together. (variables, rules, ...)
        Provides methods to do calculation with it.
        
        @ivar variables: dictionary to hold all variables.
        @type variables: E{lb}string,L{fuzzy.Variable.Variable}E{rb}
        @ivar rules: dictionary to hold all rules.
        @type rules: E{lb}string,L{fuzzy.Rule.Rule}E{rb}
        @ivar description: description
        @type description: string
    """ 

    def __init__(self,description=""):
        """Constructor.

        @param description: description
        @type description: string
        """
        self.variables = {}
        self.rules = {}
        self.description = description

    def reset(self):
        """Reset all memberships for the next run of calculate"""
        for variable in self.variables.values():
            variable.reset()

    def fuzzify(self,input):
        """Fuzzify the inputs.
        The input dictionary contains the input values for the named variables."""

        # feed input values in variables and so in adjectives
        for (name,value) in input.items():
            if name in self.variables:
                self.variables[name].setValue(value)
            #else:
            #   print "ignored input ",name


    def inference(self):
        """Calculate the fuzzy inference given by the rules."""

        # compute fuzzy rules 
        for rule in self.rules.values():
            rule.compute()


    def defuzzify(self,output):
        """Defuzzyfy the variables.
        The output dictionary serves as container and provides the names of the
        variables to read."""

        # get all wanted output variables
        for name in output.keys():
            output[name] = self.variables[name].getValue()

        return output


    def calculate(self,input,output):
        """Do a complete fuzzy calculation step.
        The input dictionary contains the input values for the named variables.
        The output dictionary serves as container and provides the names of the
        variables to read."""

        self.reset()

        self.fuzzify(input)

        self.inference()

        self.defuzzify(output)

        return output


    def findVariableName(self,var):
        """Find name of variable in this system"""
        for name,variable in self.variables.iteritems():
            if var is variable:
                return name
        return None

    def findAdjectiveName(self,adj):
        """Find name of adjective (and variable) in this system"""
        for name,variable in self.variables.iteritems():
            for namea,adjective in variable.adjectives.iteritems():
                if adj is adjective:
                    return [namea,name]
        return None

    def findRuleName(self,_rule):
        """Find name of rule in this system"""
        for name,rule in self.rules.iteritems():
            if _rule is rule:
                return name
        return None

