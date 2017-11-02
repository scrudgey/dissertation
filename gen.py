"""Code for regenerating chapter .tex file from my paper
.tex file. This makes incorporating changes easier and
avoids version confusion.
"""
import re
import ipdb

input_path = '/Users/RSHAW/science/my_papers/tq_eq/eq.tex'
output_path = '/Users/RSHAW/science/my_papers/dissertation/tex/chapter3.tex'
plot_hook = re.compile('includegraphics')
ack_hook = re.compile(r'\\acknowledgments{')
ack_end_hook = re.compile('}')
plotname_hook = re.compile('(\w+)\.pdf}')

short_caps = {
  'colormag': 'Color-magnitude diagram for the high-redshift SpARCS cluster sample',
  'colormag_dustsub': 'Dust-corrected color-magnitude diagram for the high-redshift SpARCS cluster sample',
  'sfr_model': 'Toy model of star formation history for a quenched galaxy',
  'ellipses_clustering': 'Criteria for classifying star-forming, intermediate, and quiescent galaxies based on cuts in dust-corrected color-magnitude space',
  'quenching_timescales': 'Quenching timescale as a function of redshift',
  'sfh': 'Toy model of star formation history of a quenched galaxy',
  'rgb': 'Relationship between cluster mass accretion rate and counts of galaxies in different phases of evolution',
  'fractions': 'Evolution of passive fraction within the quenching model',
  'shechter': 'Evolution of the field quiescent fraction with redshift',
  'UVJ': 'Mean binned galaxy ages in rest-frame \textit{UVJ} space'
  }



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
  lines = infile.readlines()
  start_index = -1
  end_index = -1
  print 'parsing ...'
  for i, line in enumerate(lines):
    if '\section{Introduction}' in line:
      start_index = i
    if '% end of chapter 3' in line:
      end_index = i
      break
  infile.close()

  outfile = open(output_path, 'w')
  skipping = False
  outfile.write(r"""\chapter{Quenching timescale}

\newcommand\mynote[1]{\textcolor{red}{#1}}
\newcommand\persnote[1]{\textcolor{green}{#1}}
\newcommand\tq[3]{#1\substack{+#2 \\ -#3}}
\newcommand\hiresult{$\tq{1.24}{0.23}{0.20}\ $}
\newcommand\htd{$\tq{0.94}{0.20}{0.18}$}
\newcommand\htf{ $\tq{0.29}{0.14}{0.15}$}
\newcommand\gresult{$\tq{1.50}{0.19}{0.18}\ $}
\newcommand\gtd{$\tq{0.69}{0.13}{0.13}$}
\newcommand\gtf{$\tq{0.80}{0.15}{0.18}$}
\newcommand\simhiresult{\sim1.2}
\newcommand\simgresult{\sim1.5}
\newcommand{\rpm}{\raisebox{.2ex}{$\scriptstyle\pm$}}

\def\changemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item[]}
\let\endchangemargin=\endlist
    """)

  for line in lines[start_index+1:end_index]:
    line = re.sub('deluxetable\*', 'deluxetable', line)
    line = re.sub(r'\\appendix', r'% \\appendix', line)
    if not skipping:
      if plot_hook.search(line):
        # print 'plot found: {}'.format(line)
        line = re.sub('plots/', 'figures/c2/', line)
      if ack_hook.search(line):
        # print "found acknowledgements. skipping... "
        print line
        skipping = True
        continue
      if plotname_hook.search(line):
        filename = plotname_hook.search(line).group(1)
        print 'found plot {}'.format(filename)
        capstring = 'caption[{}]'.format(short_caps[filename])
      if '\caption' in line:
        print 'caption found, subbing {}'.format(capstring)
        # capstring = 'caption[{}]'.format(short_caps.pop(-1))
        line = re.sub(r'caption', capstring, line)
        pass
      outfile.write(line)
    else:
      if ack_end_hook.search(line):
        print "ending acknowledgements."
        print line
        skipping = False
        continue

  outfile.close()

gen()
