#!/usr/bin/env python

# created 2001/08 Rene Liebscher

__revision__ = "$Id: setup.py,v 1.2 2003-02-13 08:45:30 rliebscher Exp $"

from distutils.core import setup

setup (name = "pyfuzzy",
       version = "0.0.1",
       description = "Python Fuzzy Utilities",
       author = "Rene Liebscher",
       author_email = "R.Liebscher@gmx.de",
       maintainer = "Rene Liebscher",
       maintainer_email = 'R.Liebscher@gmx.de',
       url = "http://sf.net/projects/pyfuzzy/",
       licence = "GPL",
       long_description = """...""",

       packages = ['fuzzy', 'fuzzy.set', 'fuzzy.operator', 'fuzzy.norm'],
      )
