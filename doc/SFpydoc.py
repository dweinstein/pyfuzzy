#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# Creates a pydoc documentation, but replaces all file link with links
# to the CVS repository browser
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


__revision__ = "$Id: SFpydoc.py,v 1.5 2009-08-07 07:18:09 rliebscher Exp $"

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
