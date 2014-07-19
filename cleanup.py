#!/usr/bin/python

# Node js code outputs SVG's with capital tags, so this script writes out a new file
# with them changed to lowercase

import re
import sys

svg_string = sys.argv[1]

with open(svg_string,'r') as f:
	instring = f.read()

# substitution in two passes. Make end tags lowercase, then do start tags
clean_ends = re.sub('</\w+>',lambda match: r'{}'.format(match.group().lower()),instring)
clean_total = re.sub('<\w+',lambda match: r'{}'.format(match.group().lower()),clean_ends)

with open(''.join(["clean_",svg_string]),'w') as f:
	f.write(clean_total)


