#!/usr/bin/env python
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
"""run all unit tests.
"""
__revision__ = "$Id: runtests.py,v 1.3 2010-03-28 18:47:28 rliebscher Exp $"

import unittest

import sys
import os.path
import fnmatch

# insert directory with sources at first position of python module search path
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), os.path.pardir))

try:
    # check if os.path.relpath is available
    from os.path import relpath #@UnresolvedImport
    _os_path_relpath = relpath
    del relpath
except:
    def _os_path_relpath(path,start=None):
        """\
        Own implementation of os.path.relpath which don't exist before Python 2.6.
        See U{http://docs.python.org/library/os.path.html?highlight=os.path.relpath#os.path.relpath}
        """
        if start is None:
            start = os.curdir
        path = os.path.abspath(path).split(os.sep)
        start = os.path.abspath(start).split(os.sep)
        numberCommonElements = 0
        for i in range(min(len(path),len(start))):
            if path[i] == start[i]:
                numberCommonElements += 1
            else:
                break
        path = path[numberCommonElements:]
        start = start[numberCommonElements:]
        return os.path.join(*([os.path.pardir] * len(start) + path))

def discover(top_level_dir="."):
    """\
    Find and load all unit test scripts in given directory
    """
    s = unittest.TestSuite()
    for root, dirs, files in os.walk(top_level_dir):
        testdirs = fnmatch.filter(dirs, "test_*")
        unwanteddirs = [d for d in dirs if not d in testdirs]
        for d in unwanteddirs:
            dirs.remove(d)

        for file in fnmatch.filter(files, "test_*.py"):
            path = os.path.splitext(os.path.normpath(os.path.join(root, file)))[0]
            relpath = _os_path_relpath(path, top_level_dir)
            name = relpath.replace(os.path.sep, ".")
            __import__(name) # return value is top level module, not the specified!!!
            module = sys.modules[name]
            s.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))
    return s

if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(discover(os.path.abspath(os.path.dirname(sys.argv[0]))))
    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(len(result.errors) + len(result.failures))
    #unittest.main()

