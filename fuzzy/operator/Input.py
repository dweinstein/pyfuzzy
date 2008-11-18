# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Input.py,v 1.9 2008-11-18 21:46:48 rliebscher Exp $"


from fuzzy.operator.Operator import Operator

class Input(Operator):
    """Special operator which gets it value from a fuzzy adjective.
       
       @ivar adjective: from which adjective get the membership value.
       @type adjective: instance of L{fuzzy.Adjective.Adjective}
"""

    def __init__(self,adjective):
        """Constructor.
        
        @param adjective: from which adjective get the membership value.
        @type adjective: instance of L{fuzzy.Adjective.Adjective}
        """ 
        super(Input, self).__init__()
        self.adjective = adjective

    def __call__(self):
        """return membership of given adjective."""
        return self.adjective.getMembership()
