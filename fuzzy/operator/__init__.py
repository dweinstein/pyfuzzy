# -*- coding: iso-8859-1 -*-
"""These operators are used to build fuzzy rules.

For example:

c{(A and B) or not C}

where

 - A,B,C is an adjective of a fuzzy variable and
 - 'and'/'or' are fuzzy norms

can be modelled as::

 Compound(FuzzyOr(),
     Compound(FuzzyAnd(),
         Input(A),
         Input(B)
     ),
     Not(
         Input(C)
     )
 )
"""

__revision__ = "$Id: __init__.py,v 1.3 2008-11-18 18:55:06 rliebscher Exp $"
