
__revision__ = "$Id: OutputVariableDict.py,v 1.2 2003-03-20 08:47:27 rliebscher Exp $"


from fuzzy.Variable import Variable


class OutputVariableDict(Variable):
    """Output variable which stores it adjective memberships
       in a dictionary for output.
       You should use in the adjectives instances of Set itself.
       
       What can be done with this?
       
       For example:
       You want help with buying a car.
       
       Input are your preferences:
       speed, payload (1-10), ...
       (map to "very important, important, doesn't matter, not wanted, never" ;-)
       
       Output are choices:
       cars with adjectives: ferrari, truck, ...
       
       rules are as follows:
       if speed->very_important && payload->never then car->ferrari
       if payload->very_important then car->truck
       ... and so on
       
       Then you use this as follows 
       input variables 
       { speed:3, payload:1, ...} 
       ==> 
       output_variables
       { car: {
                ferrari:0.1,
		truck: 1.0,
		...
    	      }
       }
   
       """

    def __init__(self,*args,**keywords):
        Variable.__init__(*tuple([self]+list(args)),**keywords)
        
    def getValue(self):
        """no defuzzyfication just return membership values"""
        temp = {}
        for adjective in self.adjectives.keys():
	    # get precomputed adjective set membership
    	    temp[adjective] = self.adjectives[adjective].getMembership()    
        return temp
