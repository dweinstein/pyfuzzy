# -*- coding: iso-8859-1 -*-

"""Helper functions for  pyfuzzy."""

__revision__ = "$Id: utils.py,v 1.1 2008-11-18 18:56:09 rliebscher Exp $"

def prop(func):
  """Function decorator for defining property attributes

  The decorated function is expected to return a dictionary
  containing one or more of the following pairs:
      fget - function for getting attribute value
      fset - function for setting attribute value
      fdel - function for deleting attribute
  This can be conveniently constructed by the locals() builtin
  function; see:
  http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/205183
  """
  return property(doc=func.__doc__, **func())
