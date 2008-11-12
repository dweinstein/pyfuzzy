#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# created 2001/08 Rene Liebscher

__revision__ = "$Id: setup.py,v 1.7 2008-11-12 21:54:30 rliebscher Exp $"

from distutils.core import setup

setup (name = "pyfuzzy",
       version = "0.0.3",
       description = "Python Fuzzy Utilities",
       author = "Rene Liebscher",
       author_email = "R.Liebscher@gmx.de",
       maintainer = "Rene Liebscher",
       maintainer_email = 'R.Liebscher@gmx.de',
       url = "http://sf.net/projects/pyfuzzy/",
       license = "GPL",
       long_description = """...""",

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
