#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

__revision__ = "$Id: SFpydoc.py,v 1.4 2009-01-09 22:07:06 rliebscher Exp $"

from mypydoc import MyHTMLDoc
import pydoc

class SFHTMLDoc(MyHTMLDoc):
    """Formatter class for HTML documentation."""

    SF_URL="http://pyfuzzy.cvs.sourceforge.net/viewvc/pyfuzzy/pyfuzzy%s?view=markup"
    def filelink(self,url,path):
        import os
        cwd=os.getcwd()
        cwd=cwd.replace("/doc/pydoc","")
        url=url.replace(cwd,"")
        path=path.replace(cwd,"")
        return '<a href="%s">%s</a>' % (self.SF_URL % url, path)

# --------------------------------------- interactive interpreter interface

pydoc.html = SFHTMLDoc()

if __name__ == '__main__': pydoc.cli()
