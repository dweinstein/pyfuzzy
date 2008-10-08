# -*- coding: iso-8859-1 -*-
"""These operators are used to build fuzzy rules.

For example:

(A and B) or not C

where

- A,B,C is an adjective of a fuzzy variable and
- 'and'/'or' are fuzzy norms

can be modelled as

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

__revision__ = "$Id: __init__.py,v 1.2 2008-10-08 13:14:45 rliebscher Exp $"
