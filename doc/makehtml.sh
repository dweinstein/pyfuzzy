#!/bin/bash
# $Id: makehtml.sh,v 1.5 2008-11-13 14:25:06 rliebscher Exp $

export PYTHONPATH=../..
mkdir html
cd html

# if you want create local docs replace ../mypydoc.py 
# with the path to the pydoc in your python lib directory
#PYDOC=/usr/lib/python/pydoc.py
PYDOC=../SFpydoc.py
#MODULES="fuzzy fuzzy.norm fuzzy.operator fuzzy.set fuzzy.defuzzify fuzzy.doc fuzzui ./../.."
MODULES="./../.."
for i in $MODULES ; do
    python -O $PYDOC -w $i
done
#cd ..