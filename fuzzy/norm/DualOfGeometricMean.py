from fuzzy.norm.Norm import Norm

class DualOfGeometricMean(Norm):

    def __init__(self):
        Norm.__init__(self,0) # XXX

    def __call__(self,*args):
        return 1.0 - pow(reduce(lambda x,y:x*y,
                                map(lambda x:1.0-x,
                                    args
                                   )    
                               ),1.0/len(args)) 
