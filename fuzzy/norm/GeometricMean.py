from fuzzy.norm.Norm import Norm

class GeometricMean(Norm):

    def __init__(self):
        Norm.__init__(self,0)

    def __call__(self,*args):
        return pow(reduce(lambda x,y:x*y,args),1.0/len(args)) 
