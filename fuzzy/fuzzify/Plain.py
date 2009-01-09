# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Plain.py,v 1.1 2009-01-09 22:01:35 rliebscher Exp $"


from fuzzy.fuzzify.Base import Base


class Plain(Base):
    """Just fuzzify the input value using the membership values of the given adjectives"""

    def __init__(self,*args,**keywords):
        super(Plain, self).__init__(*args,**keywords)

    def setValue(self,variable,value):
        """Let adjectives calculate their membership values."""
        for adjective in variable.adjectives.values():
            adjective.setMembershipForValue(value)
        return value
