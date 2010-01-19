#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010  Rene Liebscher
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
Unit tests for function norm in module fuzzy.set.operations
"""

__revision__ = "$Id: test_operations_norm.py,v 1.1 2010-01-19 21:51:15 rliebscher Exp $"

import unittest
from fuzzy.set.Polygon import Polygon
from fuzzy.set.operations import norm
from fuzzy.norm.Min import Min
from helper import addTests

class Function_norm(unittest.TestCase):

    patterns = {
"1": [[(1., 0.), (1., 1.), (1., 0.)], [(1., 0.), (1., 0.5), (1., 0.)], Min(), 0.5],
"2": [[(1., 0.), (1., 1.)], [(1., 0.), (1., 0.5)], Min(), 0.5],
"3": [[(1., 1.), (1., 0.)], [(1., 0.5), (1., 0.)], Min(), 0.5],
"4": [[(1., 0.), (2., 1.)], [(1., 0.), (1.5, 0.5), (2., 0.5)], Min(), 0.5],
"5": [[(1., 1.), (2., 0.)], [(1., 0.5), (1.5, 0.5), (2., 0.)], Min(), 0.5],
                }

    def template(self,i,o,n,p):
        r = norm(n, Polygon(i),p)
        self.assertEqual(o,r.points)
        
Function_norm = addTests(Function_norm)

if __name__ == '__main__':
    unittest.main()

