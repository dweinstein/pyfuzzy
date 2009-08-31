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

__revision__ = "$Id: Base.py,v 1.1 2009-08-31 21:02:06 rliebscher Exp $"

import fuzzy.Exception

class ComplementException(fuzzy.Exception.Exception):
    pass


class Base(object):
    """base class for all complement methods"""

    def __init__(self,*args,**keywords):
        super(Base, self).__init__(*args,**keywords)

    def __call__(self,value):
        """Calculate the complement of the value."""
        raise ComplementException("don't use the abstract base class")

