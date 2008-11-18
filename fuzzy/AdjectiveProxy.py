# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: AdjectiveProxy.py,v 1.7 2008-11-18 18:55:06 rliebscher Exp $"


class AdjectiveProxy(object):
    """Serves as proxy for the named variable.adjective in system.
    
    @deprecated: such objects have problems using pickle
    """

    def __init__(self,system,variable,adjective):
        self.proxy_system = system
        self.proxy_variable = variable
        self.proxy_adjective = adjective

    def __getattr__(self,name):
        """Return attribute value from real adjective."""
        if name in ["proxy_variable","proxy_adjective","proxy_system"]:
            return self.__dict__[name]
        else:
            variable = self.__dict__["proxy_variable"]
            adjective = self.__dict__["proxy_adjective"]
            system = self.__dict__["proxy_system"]
            return getattr(system.variables[variable].adjectives[adjective],name)

    def __setattr__(self,name,value):
        """Set attribute value in real adjective."""
        if name in ["proxy_variable","proxy_adjective","proxy_system"]:
            self.__dict__[name] = value
        else:
            variable = self.__dict__["proxy_variable"]
            adjective = self.__dict__["proxy_adjective"]
            system = self.__dict__["proxy_system"]
            setattr(system.variables[variable].adjectives[adjective],name,value)

    def getName(self,system):
        """Find own name in given system.
        Returns a tuple (var_name,adj_name) of None."""
        if system is self.proxy_system:
            return [self.proxy_adjective,self.proxy_variable]
        raise fuzzy.Exception.Exception()
