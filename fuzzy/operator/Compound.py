from fuzzy.operator.Operator import Operator
class Compound(Operator):
    """Take values of input operators  and process them
       through the given norm.
    """ 
    
    def __init__(self, norm, *inputs):
        Operator.__init__(self)
        self.norm = norm
        self.inputs = inputs

    def __call__(self):
        return apply(self.norm,map(lambda x:x(),self.inputs))

