from fuzzy.norm.Max import Max

class Adjective:

    # default if not set in instance
    _COM = Max()

    def __init__(self,set,COM=None):
        self.set = set
        self.membership = None
        self.COM = COM

    def setMembershipForValue(self,value):
        self.membership = self.set(value)

    def getMembership(self):
	if self.membership is None:
    	    return 0.0
	else:
	    return self.membership

    def setMembership(self,value):
        """Set membership of this adjective, if
           already set use COM norm to merge
           old and new value."""
        
        if self.membership is None:
            self.membership = value
        else:
            self.membership = (self.COM or self._COM)(
                                                    self.membership,  # consider already set value
                                                    value
                                                )

    def reset(self):
        self.membership = None