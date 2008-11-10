# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: System.py,v 1.7 2008-11-10 12:31:15 rliebscher Exp $"


class System(object):
    """Holds all stuff together. (variables, rules, ...)
       Provides methods to do calculation with it.""" 

    def __init__(self):
        """Constructor.
        Creates two instance variables:
        variables: dictionary to hold all variables.
        rules:     dictionary to hold all rules.
        """
        self.variables = {}
        self.rules = {}


    def fuzzify(self,input):
        """Fuzzify the inputs.
        The input dictionary contains the input values for the named variables."""

        # reset everything what might be left from last run
        for variable in self.variables.values():
            variable.reset()

        # feed input values in variables and so in adjectives
        for (name,value) in input.items():
            if self.variables.has_key(name):
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

        self.fuzzify(input)

        self.inference()
        
        self.defuzzify(output)

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

####################################

    def printVariablesDot(self,out):
        """   """
        for name,variable in self.variables.iteritems():
            variable.printDot(out,self,name)

    def printRulesDot(self,out):
        """   """
        for name,rule in self.rules.iteritems():
            rule.printDot(out,self,name)

    def printDot(self,out):
        """   """
        out.write(
"""digraph System {
graph [rankdir = "LR"];
""")
        #self.printVariablesDot(out)
        self.printRulesDot(out)
        out.write(
"""}
""")
