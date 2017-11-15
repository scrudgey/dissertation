#!/bin/ksh
#cp /Users/RSHAW/science/my_papers/tq_eq/mybib.bib ./tqbib.bib
#cat gclassbib.bib tqbib.bib > mybib.bib
python gen.py
pdflatex thesis
bibtex thesis
pdflatex thesis
pdflatex thesis
open thesis.pdf
