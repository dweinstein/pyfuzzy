
__revision__ = "$Id: Function.py,v 1.4 2003-06-11 13:29:11 rliebscher Exp $"


from fuzzy.set.Set import Set

class Function(Set):
    """Base class for any fuzzy set defined by a function (not a polygon)."""

    # if converted if linear polygon form use
    # at least x pieces
    _resolution = 25

    def __init__(self):
        Set.__init__(self)
