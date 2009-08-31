#!/bin/bash
#
# Creates documentation with pydoc and epydoc (PDF and HTML)
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
# $Id: makedocs.sh,v 1.2 2009-08-31 21:03:01 rliebscher Exp $

function run_pydoc {
    # this create docs with links to sourceforge cvs browser
    python ../SFpydoc.py -w $1
    # if you want create local docs uncomment the next line
    #pydoc -w $1
}

function create_pydoc {
    mkdir pydoc
    cd pydoc
    export PYTHONPATH=../..

    MODULES="./../.."
    for i in $MODULES ; do
        run_pydoc $i
    done
    cd ..
}

function create_epydoc {
    export PYTHONPATH=..
    epydoc --html -v --graph=all --redundant-details --navlink='<a class="navbar" target="_top" href="http://pyfuzzy.sourceforge.net">pyfuzzy</a> <b>/</b> <a class="navbar" target="_top" href="http://sourceforge.net/projects/pyfuzzy"><img style="border: 0px;vertical-align:bottom;padding: 2px 4px;" src="http://sflogo.sourceforge.net/sflogo.php?group_id=59160&amp;type=9" width="80" height="15" alt="Get pyfuzzy at SourceForge.net. Fast, secure and Free Open Source software downloads" /></a>' -n pyfuzzy -o epydoc fuzzy
}
function create_epydoc_pdf {
    export PYTHONPATH=..
    epydoc --pdf -v --graph=all --redundant-details -u http://pyfuzzy.sourceforge.net -n pyfuzzy -o epydoc_pdf fuzzy
}

create_pydoc

create_epydoc_pdf

create_epydoc
