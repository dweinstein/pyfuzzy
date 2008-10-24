#!/bin/bash
# $Id: makehtml.sh,v 1.4 2008-10-24 20:42:13 rliebscher Exp $

export PYTHONPATH=../..
mkdir html
cd html

# if you want create local docs replace ../mypydoc.py 
# with the path to the pydoc in your python lib directory
#PYDOC=/usr/lib/python/pydoc.py
PYDOC=../SFpydoc.py


python -O $PYDOC -w fuzzy
python -O $PYDOC -w fuzzy.norm
python -O $PYDOC -w fuzzy.operator
python -O $PYDOC -w fuzzy.set
python -O $PYDOC -w fuzzy.doc
python -O $PYDOC -w fuzzui
python -O $PYDOC -w ./../..
#cd ..