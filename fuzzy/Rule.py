from fuzzy.norm.Min import Min

class Rule:
    """This is realizes an important part of the inferenz engine.
       It represents and calculates the value of a fuzzy rule
       and sets the given adjective to the appropriate value.

       class variables:
       _CER[=Min()]: the default value for the norm used to
                     calculate the certainty of a rule.
    """
    
    # default if not set in instance
    _CER = Min()

    def __init__(self,adjective,operator,certainty=1.0,CER=None):
        """Initialize instance.
           adjective: fuzzy adjective to set
           operator: Operator which provides the value to set
           certainty: how sure are we about this rule
           CER: fuzzy norm to use with certainty (normally a t-norm)
        """
        
        self.adjective = adjective
        self.operator = operator
        self.certainty = certainty
        self.CER = CER

    def compute(self):
        """Compute and set value for given fuzzy adjective."""
        
        self.adjective.setMembership(
                                    (self.CER or self._CER)(
                                        self.certainty,       # how sure are we about this rule
                                        self.operator() # value from input
                                    )
                                )