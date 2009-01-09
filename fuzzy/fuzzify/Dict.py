# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Dict.py,v 1.1 2009-01-09 22:01:35 rliebscher Exp $"


from fuzzy.fuzzify.Base import Base


class Dict(Base):
    """Fuzzification method which gets adjective memberships
       in a dictionary instead of values to fuzzify.
       You should use in the adjectives instances of Set itself.

       Q : What can be done with this?

       A : Break complexity, by divide big and heavy fuzzy
       systems into small ones ::

        input1 ----> *******
        input2 ----> * FIS *
        input3 ----> *     * ------> output
        input4 ----> *******

       should be::

        input1 ----> *******
        input2 ----> *FIS 1* ----+
                     *******     |
                                 +--> *******
        input3 ----> ******* -------> *FIS 3* ----> output
        input4 ----> *FIS 2*          *******
                     *******
 
       Q : Why don't defuzzify outputs of FIS1 and FIS2 ?

       A : Defuzzification mean data loss.

      """

    def __init__(self,*args,**keywords):
        super(Base,self).__init__(*args,**keywords)

    def setValue(self,variable,value):
        """Do not let adjectives calculate their membership values."""
        for adjective_key in value:
            variable.adjectives[adjective_key].membership = value[adjective_key]
        return None