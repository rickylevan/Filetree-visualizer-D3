#!/usr/bin/python

# Node js code outputs SVG's with capital tags, so this script writes out a new file
# with them changed to lowercase

import re

with open('graph.svg','r') as f:
	instring = f.read()

clean_ends = re.sub('</\w+>',lambda match: r'{}'.format(match.group().lower()),instring)
clean_total = re.sub('<\w+',lambda match: r'{}'.format(match.group().lower()),clean_ends)

with open('clean_graph.svg','w') as f:
	f.write(clean_total)


