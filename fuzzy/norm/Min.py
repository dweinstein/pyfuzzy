from fuzzy.norm.Norm import Norm

class Min(Norm):

    def __init__(self):
        Norm.__init__(self,Norm.T_NORM)

    def __call__(self,*args):
	"""Return minimum of given values."""
        return min(args)
