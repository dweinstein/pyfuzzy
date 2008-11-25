# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Rule.py,v 1.10 2008-11-25 14:01:51 rliebscher Exp $"


from fuzzy.norm.Min import Min

class Rule(object):
    """This is realizes an important part of the inferenz engine.
       It represents and calculates the value of a fuzzy rule
       and sets the given adjective to the appropriate value.

       @cvar _CER: the default value (=Min()) for the norm used to calculate the certainty of a rule.
       @type _CER: L{fuzzy.norm.Norm.Norm}
       @ivar adjective: fuzzy adjective to set
       @type adjective: L{fuzzy.Adjective.Adjective}
       @ivar operator: Operator which provides the value to set
       @type operator: L{fuzzy.operator.Operator.Operator}
       @ivar certainty: how sure are we about this rule
       @type certainty: float
       @ivar CER: fuzzy norm to use with certainty (normally a t-norm)
       @type CER: L{fuzzy.norm.Norm.Norm}
    """

    # default if not set in instance
    _CER = Min()

    def __init__(self,adjective,operator,certainty=1.0,CER=None):
        """Initialize instance.
           @param adjective: fuzzy adjective to set
           @type adjective: L{fuzzy.Adjective.Adjective}
           @param operator: Operator which provides the value to set
           @type operator: L{fuzzy.operator.Operator.Operator}
           @param certainty: how sure are we about this rule
           @type certainty: float
           @param CER: fuzzy norm to use with certainty (normally a t-norm)
           @type CER: L{fuzzy.norm.Norm.Norm}
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

    def getName(self,system):
        """Lookup the name given this rule in the given system"""
        return system.findRuleName(self)
