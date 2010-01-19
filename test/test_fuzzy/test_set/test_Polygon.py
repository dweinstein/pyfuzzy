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
Unit tests for class Polygon in module fuzzy.set.Polygon
"""

__revision__ = "$Id: test_Polygon.py,v 1.1 2010-01-19 21:51:15 rliebscher Exp $"

import unittest
from fuzzy.set.Polygon import Polygon

class Method_Polygon_getValuesX(unittest.TestCase):

    def test2__(self):
        s1 = Polygon([(0.0,0.25),(1.0,0.75)])
        z = [0.0,1.0]
        #r = list(_merge_generator1(s1,s2))
        r = [x for x in s1.getValuesX()]
        self.assertEqual(z,r)

class Method_Polygon_getValuesXY(unittest.TestCase):

    def test2_(self):
        s1 = Polygon([(0.0,0.25),(1.0,0.75)])
        z = [(0.0,0.25),(1.0,0.75)]
        #r = list(_merge_generator1(s1,s2))
        r = [(x,y) for (x,y) in s1.getValuesXY()]
        self.assertEqual(z,r)

                
if __name__ == '__main__':
    unittest.main()

