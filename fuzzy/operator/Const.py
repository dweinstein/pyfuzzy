from fuzzy.operator.Operator import Operator

class Const(Operator):
    """Special operator which return a constant value."""

    def __init__(self,value):
        Operator.__init__(self)
        self.value = value

    def __call__(self):
        return self.value        