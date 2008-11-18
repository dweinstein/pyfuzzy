#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# created 2001/08 Rene Liebscher

__revision__ = "$Id: setup.py,v 1.8 2008-11-18 21:46:48 rliebscher Exp $"

from distutils.core import setup

if __name__ == "__main__":
    setup (name = "pyfuzzy",
       version = "0.0.3",
       description = "Python Fuzzy Utilities",
       author = "Rene Liebscher",
       author_email = "R.Liebscher@gmx.de",
       maintainer = "Rene Liebscher",
       maintainer_email = 'R.Liebscher@gmx.de',
       url = "http://sf.net/projects/pyfuzzy/",
       license = "LGPL",
       long_description = """pyfuzzy is a python module for working
with fuzzy sets (for example for controllers or other
similar stuff, it can be also used for decision making
in business.)
""",

       packages = [
        'fuzzy',
        'fuzzy.set',
        'fuzzy.operator',
        'fuzzy.norm',
        'fuzzy.defuzzify',
        'fuzzy.doc',
        'fuzzy.doc.plot',
        'fuzzy.doc.plot.gnuplot',
        'fuzzy.doc.structure',
        'fuzzy.doc.structure.dot',
        ],
      )
