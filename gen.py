"""Code for regenerating chapter .tex file from my paper
.tex file. This makes incorporating changes easier and
avoids version confusion.
"""
import ipdb

input_path = '/Users/RSHAW/science/my_papers/tq_eq/eq.tex'
output_path = '/Users/RSHAW/science/my_papers/dissertation/tex/chapter3.tex'

def gen():
  """Generate new chapter .tex file from paper .tex file.
  Essentially this is done by removing the paper's latex
  preamble, which is everything up to the first sentence
  of the introduction section.
  Then, we prepend a section of command definitions that need
  to be here.
  Lastly, remove the end document command.
  Write the whole thing to chapter3.tex and it'll be automatically
  included when the dissertation is recompiled.
  """
  infile = open(input_path, 'r')
  ipdb.set_trace()
  infile.close()

  outfile = open(output_path, 'w')
  outfile.close()
