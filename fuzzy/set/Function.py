
__revision__ = "$Id: Function.py,v 1.3 2003-03-20 08:47:27 rliebscher Exp $"


from fuzzy.set.Set import Set

class Function(Set):
    """Base class for any fuzzy set defined by a function (not a polygon)."""

    # if converted if linear polygon form use
    # at least x pieces
    _resolution = 25

    def __init__(self):
        Set.__init__(self)
