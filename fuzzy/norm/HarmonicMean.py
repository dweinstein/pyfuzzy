from fuzzy.norm.Norm import Norm

class HarmonicMean(Norm):

    def __init__(self):
        Norm.__init__(self,0)

    def __call__(self,*args):
        return float(len(args))/reduce(lambda x,y:x+y,
                                       map(lambda x:1.0/x,
                                           args
                                          )
                                      ) 
