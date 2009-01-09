#!/bin/bash
# $Id: makehtml.sh,v 1.7 2009-01-09 22:07:06 rliebscher Exp $

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
    epydoc --html -v --graph=all --redundant-details -u http://pyfuzzy.sourceforge.net -n pyfuzzy -o epydoc fuzzy
}
function create_epydoc_pdf {
    export PYTHONPATH=..
    epydoc --pdf -v --graph=all --redundant-details -u http://pyfuzzy.sourceforge.net -n pyfuzzy -o epydoc_pdf fuzzy
}

create_pydoc

create_epydoc_pdf

create_epydoc
