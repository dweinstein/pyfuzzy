# -*- coding: iso-8859-1 -*-
#
# Copyright (C) 2009  Rene Liebscher
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free 
# Software Foundation; either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>. 
#
"""
Helper functions for calculation with fuzzy sets.

Examples can be found here U{http://pyfuzzy.sourceforge.net/demo/merge/}

* Intersection of set1 and set2 can be done by
  
  C{set = merge(T_NORM,set1,set2)}
  
  where T_NORM is a t-norm eg. Min.
  (or a function which accepts two parameters as min().)

* Union of set1 and set2 can be done by
  
  C{set = merge(S_NORM,set1,set2)}
  
  where S_NORM is a s-norm eg. Max.
  (or a function which accepts two parameters as max().)

* Complement of set1 can be done by
  
  C{set = norm(lambda a,b:1.0-a ,set1,0.0)}
  
  using a user defined function for it.
  (The second parameter is ignored or better said
  it doesn't influence the value, it only influences
  maybe where the points of the resulting polygon are
  set.)

* Activation function can be done by
  
  C{set = norm(act_norm,set,act_value)}
  
  where act_norm is any L{fuzzy.norm} or two params function (eg. min)
  and act_value is the result of a rule calculation.
"""

__revision__ = "$Id: operations.py,v 1.7 2009-10-23 19:20:03 rliebscher Exp $"

# helper functions
def _find_root(f, x1, x2, f1=None, f2=None, epsilon=None):
    """Find root of function f between x1,x2 by using the regula falsi method.
       The algorithm stops if the error estimation is smaller than epsilon
       or there is an ZeroDivisionError, which means both values f1 and f2 are 
       identical (should be 0 then).
           
       @param f: function for which to find M{f(x)=0}
       @type f: M{f(x)}
       @param x1: left border of range
       @type x1: float
       @param x2: right border of range
       @type x2: float
       @param f1: value for x1, if available
       @type f1: float
       @param f2: value for x2, if available
       @type f2: float
       @param epsilon: break condition for algorithm (value < epsilon)
       @type epsilon: float/None
       @return: M{x} where M{f(x)=0}
       @rtype: float
    """
    if f1 is None:
        f1 = f(x1)
    if f2 is None:
        f2 = f(x2)
    if f1 * f2 > 0.:
        raise Exception("need interval with root")
    if epsilon is None:
        epsilon = 1.e-10
    epsx = epsz = epsilon
    z = (x1+x2)/2.
    try:
        for i in xrange(1000):
            z = x1 - f1 * (x2 - x1) / (f2 - f1) # approximation for root
            fz = f(z)
        
            #print x1,z,x2,f1,fz,f2
            # smaller than epsilon: return z as approximation
            if abs(x2 - x1) <= epsx or abs(fz) <= epsz:
                return z
        
            # root in [f(xz), f(x2)]?: 
            if fz * f2 < 0.:
                # check [z, x2]
                x1,x2,f1,f2 = z,x2,fz,f2
            else:
                # check [x1, z]
                x1,x2,f1,f2 = x1,z,f1,fz
        raise Exception("Too much iterations: %d" % i)
    except ZeroDivisionError:
        #print "ZeroDivisionError"
        return z
    
    
def _merge_generator(NORM, set1, set2):
    """Returns a new fuzzy set which is the merger of set1 and set2,
    where the membership of the result set is equal to C{NORM(set1(x),set2(x))}.
    
    @param NORM: fuzzy norm to calculate both sets values. For example Min(), Max(), ...
        Also possible as two params function, eg. C{lambda a,b: (a+b)/2.}.
    @type NORM: L{fuzzy.norm.Norm.Norm}
    @param set1: fuzzy set
    @type set1: L{fuzzy.set.Set}
    @param set2: fuzzy set
    @type set2: L{fuzzy.set.Set}
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
       """
    from fuzzy.set.Polygon import Polygon
    g1 = set1.getIntervalGenerator()
    g2 = set2.getIntervalGenerator()

    x = g1.nextInterval(None, None)
    x_ = g2.nextInterval(None, x)
    if x_ is not None and x_ < x:
        x = x_
    if x is None:
        return
    y1 = set1(x)
    y2 = set2(x)
    yield (x, NORM(y1, y2))
    use_find_root = not (isinstance(set1, Polygon) and isinstance(set2, Polygon))
    while 1:
        prev_x, prev_y1, prev_y2 = x, y1, y2
        # get new interval from sets
        x = g1.nextInterval(prev_x, None)
        x_ = g2.nextInterval(prev_x, x)
        if x is None and x_ is None: # no need for more intervals
            break
        if x is None: 
            # first set is finished => take values from second 
            x = x_
        else:
            if x_ is None:
                # second set is finished first, x is already ok
                pass
            else:
                if x_ < x:
                    # both need more calculations, get smaller value
                    x = x_
        y1 = set1(x)
        y2 = set2(x)
        # test if intersection => split interval
        if (x != prev_x) and ((y1>y2 and prev_y1<prev_y2) or (y1<y2 and prev_y1>prev_y2)):
            # calculate intersection
            if use_find_root:
                f = lambda x,set1=set1,set2=set2:set1(x)-set2(x)
                x_ = _find_root(f, prev_x, x, prev_y1-prev_y2, y1-y2)
            else:
                y_diff = y1-y2
                prev_y_diff = prev_y2-prev_y1
                p = prev_y_diff/(prev_y_diff + y_diff)
                x_ = prev_x + p * (x-prev_x)
            y1_ = set1(x_)
            y2_ = set2(x_)
            # add this point
            yield (x_, NORM(y1_, y2_))
            # set saved point to intermediate
            prev_x, prev_y1, prev_y2 = x_, y1_, y2_
        # add this point
        yield (x, NORM(y1, y2))
    return


def merge(NORM, set1, set2, segment_size=None):
    """Returns a new fuzzy set which ist the merger of set1 and set2,
    where the membership of the result set is equal to C{NORM(set1(x),set2(x))}.
    
    For nonlinear operations you might want set the segment size to a value 
    which controls how large a linear segment of the result can be. 
    See also the following examples:
      - U{http://pyfuzzy.sourceforge.net/demo/merge/AlgebraicProduct_d_d.png} - The algebraic product is M{x*y}, so using it on the same set, it calculates the square of it.
      - U{http://pyfuzzy.sourceforge.net/demo/merge/AlgebraicSum_d_d.png} - The algebraic sum is M{x+y-x*y}.
       
    @param NORM: fuzzy norm to calculate both sets values. For example Min(), Max(), ...
        Also possible as two params function, eg. C{lambda a,b: (a+b)/2.}.
    @type NORM: L{fuzzy.norm.Norm.Norm}
    @param set1: fuzzy set
    @type set1: L{fuzzy.set.Set}
    @param set2: fuzzy set
    @type set2: L{fuzzy.set.Set}
    @param segment_size: maximum size of a segment
    @type segment_size: float/None
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
       """
    from fuzzy.set.Polygon import Polygon
    ret = Polygon()

    prev_x, prev_y = None, None
    for x, y in _merge_generator(NORM, set1, set2):
        if (segment_size is not None) and (prev_x is not None) and (abs(y-prev_y)>0.01):
            diff = x-prev_x
            if  diff > 2.*segment_size:
                n = int(diff/segment_size)
                dx = diff/n
                for i in range(1, n):
                    x_ = prev_x+i*dx
                    ret.add(x_, NORM(set1(x_), set2(x_)))
        ret.add(x, y)
        prev_x, prev_y = x, y

    return ret


def _norm_generator(NORM, set, value):
    """Returns a new fuzzy set which ist this set normed with value.
    where the membership of the result set is equal to C{NORM(set(x),value)}.
    
    @param NORM: fuzzy norm to calculate set's values with value. For example Min(), Max(), ...
        Also possible as two params function, eg. C{lambda a,b: (a+b)/2.}.
    @type NORM: L{fuzzy.norm.Norm.Norm}
    @param set: fuzzy set
    @type set: L{fuzzy.set.Set}
    @param value: value
    @type value: float
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
    """
    from fuzzy.set.Polygon import Polygon
    g = set.getIntervalGenerator()

    x = g.nextInterval(None, None)
    if x is None:
        return
    y = set(x)
    yield (x, NORM(y, value))
    use_find_root = not isinstance(set, Polygon)
    while 1:
        prev_x, prev_y = x, y
        # get new interval from sets
        x = g.nextInterval(prev_x, None)
        if x is None: # no need for more intervals
            break
        y = set(x)
        # test if intersection => split interval
        if (x != prev_x) and ((y>value and prev_y<value) or (y<value and prev_y>value)):
            # calculate intersection
            if use_find_root:
                f = lambda x,set=set:set(x)-value
                x_ = _find_root(f, prev_x, x, prev_y-value, y-value)
            else:
                y_diff = y-value
                prev_y_diff = value-prev_y
                p = prev_y_diff/(prev_y_diff + y_diff)
                x_ = prev_x + p * (x-prev_x)
            y_ = set(x_)
            # add this point
            yield (x_, NORM(y_, value))
            # set saved point to intermediate
            prev_x, prev_y = x_, y_
        # add this point
        yield (x, NORM(y, value))
    return

def norm(NORM, set, value, segment_size=None):
    """Returns a new fuzzy set which ist this set normed with value.
    where the membership of the result set is equal to C{NORM(set(x),value)}.

    For meaning of segment_size see also L{fuzzy.set.operations.merge}.
    
    @param NORM: fuzzy norm to calculate set's values with value. For example Min(), Max(), ...
        Also possible as two params function, eg. C{lambda a,b: (a+b)/2.}.
    @type NORM: L{fuzzy.norm.Norm.Norm}
    @param set: fuzzy set
    @type set: L{fuzzy.set.Set}
    @param value: value
    @type value: float
    @param segment_size: maximum size of a segment
    @type segment_size: float/None
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
    """
    from fuzzy.set.Polygon import Polygon
    ret = Polygon()

    prev_x, prev_y = None, None
    for x, y in _norm_generator(NORM, set, value):
        if (segment_size is not None) and (prev_x is not None) and (abs(y-prev_y)>0.01):
            diff = x-prev_x
            if  diff > 2.*segment_size:
                n = int(diff/segment_size)
                dx = diff/n
                for i in range(1, n):
                    x_ = prev_x+i*dx
                    ret.add(x_, NORM(set(x_), value))
        ret.add(x, y)
        prev_x, prev_y = x, y

    return ret

def _complement_generator(COMPLEMENT, set):
    """Returns a new fuzzy set which ist this complement of the given set.
    (Where the membership of the result set is equal to C{COMPLEMENT(set(x))}.
    
    @param COMPLEMENT: fuzzy complement to use. For example Zadeh(), ...
        Also possible as one param function, eg. C{lambda x: 1.-x}.
    @type COMPLEMENT: L{fuzzy.complement.Base.Base}
    @param set: fuzzy set
    @type set: L{fuzzy.set.Set}
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
    """
    g = set.getIntervalGenerator()

    x = g.nextInterval(None, None)
    if x is None:
        return
    y = set(x)
    yield (x, COMPLEMENT(y))
    while 1:
        prev_x = x
        # get new interval from sets
        x = g.nextInterval(prev_x, None)
        if x is None: # no need for more intervals
            break
        y = set(x)
        # add this point
        yield (x, COMPLEMENT(y))
    return


def complement(COMPLEMENT, set, segment_size=None):
    """Returns a new fuzzy set which ist this complement of the given set.
    (Where the membership of the result set is equal to C{COMPLEMENT(set(x))}.

    For meaning of segment_size see also L{fuzzy.set.operations.merge}.
    
    @param COMPLEMENT: fuzzy complement to use. For example Zadeh(), ...
        Also possible as one param function, eg. C{lambda x: 1.-x}.
    @type COMPLEMENT: L{fuzzy.complement.Base.Base}
    @param set: fuzzy set
    @type set: L{fuzzy.set.Set}
    @param segment_size: maximum size of a segment
    @type segment_size: float/None
    @return: resulting fuzzy set
    @rtype: L{fuzzy.set.Polygon.Polygon}
    """
    from fuzzy.set.Polygon import Polygon
    ret = Polygon()

    prev_x, prev_y = None, None
    for x, y in _complement_generator(COMPLEMENT, set):
        if (segment_size is not None) and (prev_x is not None) and (abs(y-prev_y)>0.01):
            diff = x-prev_x
            if  diff > 2.*segment_size:
                n = int(diff/segment_size)
                dx = diff/n
                for i in range(1, n):
                    x_ = prev_x+i*dx
                    ret.add(x_, COMPLEMENT(set(x_)))
        ret.add(x, y)
        prev_x, prev_y = x, y

    return ret
