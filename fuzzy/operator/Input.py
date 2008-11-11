# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Input.py,v 1.7 2008-11-11 12:19:11 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Input(Operator):
    """Special operator which gets it value from a fuzzy adjective."""

    def __init__(self,adjective):
        """Constructor.
        adjective: from which adjective get the membership value.""" 
        super(Input, self).__init__()
        self.adjective = adjective

    def __call__(self):
        """return membership of given adjective."""
        return self.adjective.getMembership()

    def printDot(self,out,system,parent_name):
        return self.adjective.printDot(out,system,parent_name)
