# -*- coding: utf-8 -*-
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
"""\
Helper functions for unit tests
"""

__revision__ = "$Id: helper.py,v 1.1 2010-01-19 21:51:15 rliebscher Exp $"


def addTests(original_class):
    """\
    Use the dictionary pattern in original_class to add 
    more methods which call the method template in original_class
    with the given parameters from pattern.
    """
    for name,args in original_class.patterns.items():
        f = lambda self,args=args: original_class.template(self,*args)
        #f.__doc__ = "generated from test case '%s'" % name
        setattr(original_class,"test"+name,f)
    return original_class
