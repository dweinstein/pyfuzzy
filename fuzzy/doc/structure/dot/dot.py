# -*- coding: iso-8859-1 -*-
"""Generates description of structure in dot format"""

__revision__ = "$Id: dot.py,v 1.3 2008-12-26 17:51:33 rliebscher Exp $"

# stores handler of different object types
_registered_handler = {}

def register_handler(class_, handler):
    _registered_handler[class_] = handler


def print_dot(obj,out,system,parentname):
    """Print object obj into output stream out"""
    for class_ in type(obj).mro():
        if class_ in _registered_handler.keys():
            handler = _registered_handler[class_]
            return handler(obj,out,system,parentname)
    return ""

def printVariablesDot(system,out):
    """Print all variables"""
    for name,variable in system.variables.items():
        print_dot(variable,out,system,name)

def printRulesDot(system,out):
    """Print all rules"""
    for name,rule in system.rules.items():
        print_dot(rule,out,system,name)

def printDot(system,out):
    """Print whole system into one graph"""
    print_header(out)
    #printVariablesDot(system,out)
    printRulesDot(system,out)
    print_footer(out)

def print_header(out,name="System"):
    """Print graph header"""
    out.write("digraph %s {graph [rankdir = \"LR\"];\n" % name)

def print_footer(out):
    """Print graph footer"""
    out.write("}\n")

# import handlers for object types
import fuzzy.doc.structure.dot.handlers
