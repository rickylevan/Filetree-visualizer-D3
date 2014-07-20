#!/usr/bin/python

# Here is the driver script. It should grab the filetree data from the OS, format it in a way
# expected by demo.js, then call demo.js, then call the cleanup script to make svg tags
# lowercase. Finally trigger "open -a Firefox fs.svg" to use the browser as a rendering tool
# for the image.

import os
import sys
import json

# run through with recursion limit
# thanks to nosklo on stack overflow
def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

# if no path argument is specified
if len(sys.argv) == 1:
	root = os.getcwd()
# if a path is specified
else:
	root = sys.argv[1]

# Now, from root, our goal is to assemble JSON like in the flare.json example.
# It should be most natural to use internal Python lists and dictionaries, and then 
# do a json.dump to get the resulting string. 


# For now, assume max recursion, with an arbitrarily large level:
level = 10

fs = walklevel(root,level)

for thing in fs:
	print thing
	print "***"
