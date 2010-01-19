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
Unit tests for function merge in module fuzzy.set.operations
"""

__revision__ = "$Id: test_operations_merge.py,v 1.1 2010-01-19 21:51:15 rliebscher Exp $"

import unittest
from fuzzy.set.Polygon import Polygon
from fuzzy.set.operations import merge,check,_merge_generator1
from fuzzy.norm.Min import Min
from fuzzy.norm.AlgebraicProduct import AlgebraicProduct
from helper import addTests

class Function_merge(unittest.TestCase):

    patterns = {
"1": [[(1.,0.),(2.,1.)], [(1.,0.),(2.,1.)], [(1.,0.),(2.,1.)], Min()],
"2": [[(1.,0.),(2.,1.)], [(2.,0.),(3.,1.)], [(1.,0.),(2.,0.),(3.,1.)], Min()],
"3": [[(1.,0.),(2.,1.)], [(1.,1.),(2.,1.)], [(1.,0.),(2.,1.)], Min()],
"4": [[(1.,0.),(2.,1.)], [(1.,1.),(2.,0.)], [(1.,0.),(1.5,0.5),(2.,0.)], Min()],
"5": [[(1.,0.),(2.,1.)], [(1.,1.),(2.,0.)], [(1.,0.),(1.5,0.25),(2.,0.)], AlgebraicProduct()],
                }

    def template(self,x1,x2,y,n):
        r = merge(n,Polygon(x1), Polygon(x2))
        self.assertEqual(y,r.points)

Function_merge = addTests(Function_merge)

class Function__check(unittest.TestCase):

    patterns = {
"1": [0.0, 0.5, 0.25, [(0.0, 0.5, 0.25)]],
"2": [0.0, [0.5], 0.25, [(0.0, 0.5, 0.25)]],
"3": [0.0, 0.5, [0.25], [(0.0, 0.5, 0.25)]],
"4": [0.0, [0.5], [0.25], [(0.0, 0.5, 0.25)]],
"5": [0.0, [0.5], [0.25, 0.5], [(0.0, 0.5, 0.25), (0.0, 0.5, 0.5)]],
"6": [0.0, [0.5], [0.25, 0.5, 1.0], [(0.0, 0.5, 0.25), (0.0, 0.5, 0.5), (0.0, 0.5, 1.0)]],
"7": [0.0, [0.5], [0.125, 0.25, 0.5, 1.0], [(0.0, 0.5, 0.125), (0.0, 0.5, 0.25), (0.0, 0.5, 0.5), (0.0, 0.5, 1.0)]],
"8": [0.0, [0.5, 0.75], [0.125, 0.25], [(0.0, 0.5, 0.125), (0.0, 0.75, 0.25)]],
"9": [0.0, [0.5, 0.75], [0.125, 0.25, 1.0], [(0.0, 0.5, 0.125), (0.0, 0.75, 0.25), (0.0, 0.75, 1.0)]],
"10": [0.0, [0.5, 0.75, 1.0], [0.125, 0.25, 0.5], [(0.0, 0.5, 0.125), (0.0, 0.75, 0.25), (0.0, 1.0, 0.5)]],
                }

    def template(self,x,y1,y2,z):
        r = list(check(x,y1,y2))
        self.assertEqual(z,r)
        
Function__check = addTests(Function__check)


class Function__merge_generator1(unittest.TestCase):

    patterns = {
"1": [[(0.0, 0.0)], [(1.0, 1.0)], [(0.0, 0.0, 1.0), (1.0, 0.0, 1.0)]],
"2": [[(0.0, 0.25), (1.0, 0.75)], [(0.0, 0.25), (1.0, 0.75)], [(0.0, 0.25, 0.25), (1.0, 0.75, 0.75)]],

"3a": [[(0.0, 0.0), (3.0, 3.0)], [(1.0, 1.0), (2.0, 2.0)], [(0.0, 0.0, 1.0), (1.0, 1.0, 1.0), (2.0,2.0,2.0), (3.0,3.0,2.0)]],
"3b": [[(1.0, 1.0), (2.0, 2.0)], [(0.0, 0.0), (3.0, 3.0)], [(0.0, 1.0, 0.0), (1.0, 1.0, 1.0), (2.0,2.0,2.0), (3.0,2.0,3.0)]],
                }

    def template(self,s1,s2,z):
        r = [a for a in _merge_generator1(Polygon(s1),Polygon(s2))]
        self.assertEqual(z,r)
        
Function__merge_generator1 = addTests(Function__merge_generator1)
                
if __name__ == '__main__':
    unittest.main()

