from fuzzy.norm.Norm import Norm

class ArithmeticMean(Norm):

    def __init__(self):
        Norm.__init__(self,0)

    def __call__(self,*args):
        return reduce(lambda x,y:x+y,args)/float(len(args)) 
