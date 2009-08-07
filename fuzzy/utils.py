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
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License along with 
# this program; if not, see <http://www.gnu.org/licenses/>. 
#

"""Helper functions for  pyfuzzy."""

__revision__ = "$Id: utils.py,v 1.3 2009-08-07 07:19:18 rliebscher Exp $"

def prop(func):
  """Function decorator for defining property attributes

  The decorated function is expected to return a dictionary
  containing one or more of the following pairs:
    - fget - function for getting attribute value
    - fset - function for setting attribute value
    - fdel - function for deleting attribute
  This can be conveniently constructed by the locals() builtin
  function; see:
  U{http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/205183}
  """
  return property(doc=func.__doc__, **func())
