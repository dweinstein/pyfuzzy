# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: Dict.py,v 1.4 2009-01-09 22:01:35 rliebscher Exp $"

class Dict(object):
    """Not a real defuuzyfication.
       Just stores the adjective memberships
       in a dictionary for output.
       You should use in the adjectives instances of Set itself.
       
       What can be done with this?
       
       For example:
       
       You want help with buying a car.
       
       Input are your preferences::
        speed, payload (1-10), ...
       (map to "very important, important, doesn't matter, not wanted, never" ;-)
       
       Output are choices:
       cars with adjectives: ferrari, truck, ...
       
       rules are as follows::
        if speed->very_important && payload->never then car->ferrari
        if payload->very_important then car->truck
       ... and so on
       
       Then you use this as follows::
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

    def getValue(self,variable):
        """no defuzzification just return membership values"""
        temp = {}
        for name,adjective in variable.adjectives.items():
            # get precomputed adjective set membership
            temp[name] = adjective.getMembership()
        return temp
