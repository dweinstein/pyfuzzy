from fuzzy.operator.Operator import Operator
class Not(Operator):
    """Take value of input operator and negate it.""" 
    
    def __init__(self, inputs):
        Operator.__init__(self)
        self.input = input

    def __call__(self):
        return 1.0 - input()

