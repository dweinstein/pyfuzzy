#!/bin/bash
# $Id: makehtml.sh,v 1.6 2008-11-18 21:46:48 rliebscher Exp $


function create_pydoc {
    mkdir pydoc
    cd pydoc
    export PYTHONPATH=../..

    # if you want create local docs replace ../mypydoc.py 
    # with the path to the pydoc in your python lib directory
    #PYDOC=/usr/lib/python/pydoc.py
    PYDOC=../SFpydoc.py
    #MODULES="fuzzy fuzzy.norm fuzzy.operator fuzzy.set fuzzy.defuzzify fuzzy.doc fuzzui ./../.."
    MODULES="./../.."
    for i in $MODULES ; do
        python $PYDOC -w $i
    done
    cd ..
}

function create_epydoc {
    export PYTHONPATH=..
    epydoc --html -v --graph=all -u http://pyfuzzy.sourceforge.net -n pyfuzzy -o epydoc fuzzy
}
function create_epydoc_pdf {
    export PYTHONPATH=..
    epydoc --pdf -v --graph=classtree -u http://pyfuzzy.sourceforge.net -n pyfuzzy -o epydoc_pdf fuzzy
}

#create_pydoc

#create_epydoc_pdf

create_epydoc
