#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# Helper utilities for tests.
#  - Find all classes in directory and return creates instances of them.
#
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


__revision__ = "$Id: utils.py,v 1.3 2009-08-31 20:57:49 rliebscher Exp $"

def get_classes(package):
    """Find all classes defined in given directory
    and return them as dictionary {name,instance}"""
    import os,imp
    package_name = package.__name__
    classes_dir = os.path.dirname(package.__file__)
    suffixes = []
    for suffix in imp.get_suffixes():
        suffixes.append(suffix[0])
    objects = {}
    for class_file in os.listdir(classes_dir):
        for suffix in suffixes:
            class_name = class_file[:-len(suffix)]
            if class_name == "__init__":
                break
            if  class_file[-len(suffix):] == suffix:
                module = __import__(package_name+"."+class_name)
                components = (package_name+"."+class_name).split('.')
                for comp in components[1:]:
                    module = getattr(module, comp)
                try:
                    objects.update({class_name: module.__dict__[class_name]()})
                except:
                    # probably no object with this name in file
                    pass
                break
    return objects
