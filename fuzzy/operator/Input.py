from fuzzy.operator.Operator import Operator

class Input(Operator):
    """Special operator which gets it value from a fuzzy adjective."""

    def __init__(self,adjective):
        Operator.__init__(self)
        self.adjective = adjective

    def __call__(self):
        return self.adjective.getMembership()        