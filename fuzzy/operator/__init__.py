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