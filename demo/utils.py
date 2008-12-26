#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: utils.py,v 1.1 2008-12-26 18:14:24 rliebscher Exp $"

def get_classes(package):
    """Find all classes defined in given directory
    and return them as dictionary {name,instance}"""
    import os,sys,imp
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
