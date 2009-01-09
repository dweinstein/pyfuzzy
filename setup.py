#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""pyfuzzy: Python Fuzzy Utilities

pyfuzzy is a python module for working with fuzzy sets 
(for example for controllers or other similar stuff, 
it can be also used for decision making in business.)
"""
__revision__ = "$Id: setup.py,v 1.9 2009-01-09 22:11:18 rliebscher Exp $"

from distutils.core import setup

DOCLINES = __doc__.split("\n")

CLASSIFIERS = """\
Development Status :: 4 - Beta
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
Programming Language :: Python
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: OS Independent
"""

PACKAGES = [
        'fuzzy',
        'fuzzy.set',
        'fuzzy.operator',
        'fuzzy.norm',
        'fuzzy.fuzzify',
        'fuzzy.defuzzify',
        'fuzzy.storage',
        'fuzzy.storage.fcl',
        'fuzzy.doc',
        'fuzzy.doc.plot',
        'fuzzy.doc.plot.gnuplot',
        'fuzzy.doc.structure',
        'fuzzy.doc.structure.dot',
        ]
	
if __name__ == "__main__":
    setup (name = "pyfuzzy",
       version = "0.1.0",
       description = DOCLINES[0],
       author = "Rene Liebscher",
       author_email = "R.Liebscher@gmx.de",
       maintainer = "Rene Liebscher",
       maintainer_email = 'R.Liebscher@gmx.de',
       url = "http://pyfuzzy.sourceforge.net",
       download_url = "http://sourceforge.net/project/showfiles.php?group_id=59160&package_id=55171",
       license = "LGPL",
       long_description = "\n".join(DOCLINES[2:]),
       classifiers=filter(None, CLASSIFIERS.split('\n')),
       platforms = ["OS Independent"],
       packages = PACKAGES,
      )
