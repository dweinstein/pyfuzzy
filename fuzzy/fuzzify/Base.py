# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Base.py,v 1.1 2009-01-09 22:01:35 rliebscher Exp $"


class Base(object):
    """base class for all fuzzification methods"""

    def __init__(self,*args,**keywords):
        super(Base, self).__init__(*args,**keywords)

    def setValue(self,variable,value):
        pass
