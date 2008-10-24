# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: SFpydoc.py,v 1.1 2008-10-24 20:42:13 rliebscher Exp $"


import sys, imp, os, stat, re, types, inspect
from repr import Repr
from string import expandtabs, find, join, lower, split, strip, rfind, rstrip

from pydoc import *
import pydoc
from mypydoc import *

class SFHTMLDoc(MyHTMLDoc):
    """Formatter class for HTML documentation."""

    def filelink(self,url,path):
        import string
        cwd=os.getcwd()
        cwd=string.replace(cwd,"/doc/html","")
        url=string.replace(url,cwd,"")
        path=string.replace(path,cwd,"")
        return '<a href="http://pyfuzzy.cvs.sourceforge.net/viewvc/pyfuzzy/pyfuzzy%s?view=markup">http://pyfuzzy.cvs.sourceforge.net/cgi-bin/viewcvs.cgi/pyfuzzy/pyfuzzy%s</a>' % (url, path)

# --------------------------------------- interactive interpreter interface

pydoc.html = SFHTMLDoc()

if __name__ == '__main__': cli()
