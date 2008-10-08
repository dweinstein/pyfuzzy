#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# created 2001/08 Rene Liebscher

__revision__ = "$Id: setup.py,v 1.4 2008-10-08 14:53:50 rliebscher Exp $"

from distutils.core import setup

setup (name = "pyfuzzy",
       version = "0.0.2",
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
