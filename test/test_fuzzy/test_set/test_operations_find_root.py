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
Unit tests for function find_root in module fuzzy.set.operations
"""

__revision__ = "$Id: test_operations_find_root.py,v 1.1 2010-01-19 21:51:15 rliebscher Exp $"

import unittest
from fuzzy.set.operations import _find_root
from helper import addTests

def f1(x):
    return x

def f2(x):
    return x+1

def f3(x):
    return x*x

def f4(x):
    return x*x-1

class Function__find_root(unittest.TestCase):

    patterns = {
               "1": [0., f1, 0., 0.],
               "1a": [0., f1, 0., 1.],
               "1b": [0., f1, -1., 0.],
               "1c": [0., f1, -1., 1.],
               "2a": [-1., f2, -2, 0.],
               "2b": [-1., f2, -2., 1],
               "3": [0., f3, -1., 1.],
               "4": [0., f3, +1., +2],
               "5": [-1., f4, -3.3, 0.],
               "6": [-1., f4, -0.3, 0.],
               "7": [+1., f4, +0.3, 5.],
               "8": [+1., f4, +3.3, 5.],
               }

    def template(self,x,f,x1,x2):
        self.assertAlmostEqual(x, _find_root(f, x1, x2))
    
Function__find_root = addTests(Function__find_root)

if __name__ == '__main__':
    unittest.main()

