
class System:
    """Holds all stuff together. (variables, rules, ...)
       Provides methods to do calculation with it.""" 
    
    def __init__(self):
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