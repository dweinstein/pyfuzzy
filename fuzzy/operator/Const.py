from fuzzy.operator.Operator import Operator

class Const(Operator):
    """Special operator which return a constant value."""

    def __init__(self,value):
	"""Constructor.
	value: value returned at call of __call__()."""
        Operator.__init__(self)
        self.value = value

    def __call__(self):
	"""Return stored constant value."""
        return self.value        