from fuzzy.norm.Norm import Norm

class Max(Norm):

    def __init__(self):
        Norm.__init__(self,Norm.S_NORM)

    def __call__(self,*args):
        return max(args)
