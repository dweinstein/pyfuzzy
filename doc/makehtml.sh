#!/bin/bash
export PYTHONPATH=../..
mkdir html
cd html

# if you want create local docs replace ../mypydoc.py 
# with the path to the pydoc in your python lib directory

python -O ../mypydoc.py -w fuzzy
python -O ../mypydoc.py -w fuzzy.norm
python -O ../mypydoc.py -w fuzzy.operator
python -O ../mypydoc.py -w fuzzy.set
python -O ../mypydoc.py -w ./../..
#cd ..