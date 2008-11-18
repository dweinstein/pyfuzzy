# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: InputVariableDict.py,v 1.4 2008-11-18 18:55:06 rliebscher Exp $"


from fuzzy.InputVariable import InputVariable


class InputVariableDict(InputVariable):
    """Input variable which provides adjective memberships
       in a dictionary instead of values to fuzzyfy.
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
 
       Q : Why don't deffuzzyfy outputs of FIS1 and FIS2 ?

       A : Defuzzyfication mean data loss.

      """

    def __init__(self,*args,**keywords):
        InputVariable.__init__(*tuple([self]+list(args)),**keywords)

    def setValue(self, value):
        """Do not let adjectives calculate their membership values."""
        self.__value = None
        for adjective_key in value:
            self.adjectives[adjective_key].membership = value[adjective_key]
