class AdjectiveProxy:
    """Serves as proxy for the named variable.adjective in system."""

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
