# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Function.py,v 1.8 2008-11-18 21:46:48 rliebscher Exp $"


from fuzzy.set.Set import Set

class Function(Set):
    """Base class for any fuzzy set defined by a function (not a polygon)."""

    # if converted if linear polygon form use
    # at least x pieces
    _resolution = 25 #: segments when converting into a polygon
