class Variable:
    """Base class for any kind of fuzzy variable.
       Returns as output the previous input value."""

    def __init__(self):
        self.adjectives = {}
        self.__value = None
        
    def setValue(self,value):
        """Let adjectives calculate their membership values."""
        self.__value = value
        for adjective in self.adjectives.values():
            adjective.setMembershipForValue(value)

    def getValue(self):
        """Return previous input value."""
        return self.__value

    def reset(self):
        """Reset meberships of adjectives for new calculation step."""
        for adjective in self.adjectives.values():
            adjective.reset()
