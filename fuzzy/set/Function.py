from fuzzy.set.Set import Set

class Function(Set):

    # if converted if linear polygon form use
    # at least x pieces
    _resolution = 25

    def __init__(self):
        Set.__init__(self)
