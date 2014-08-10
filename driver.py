#!/usr/bin/python

# Plan of attack (not yet coded up)
# Here is the driver script. It should grab the filetree data from the OS, format it in a way
# expected by demo.js, then call demo.js, then call the cleanup script to make svg tags
# lowercase. Finally trigger "open -a Firefox fs.svg" to use the browser as a rendering tool
# for the image.

import os
import sys
import json

def get_dir_name():
	return os.getcwd().split('/')[-1]

# find out how many terms in absolute path must be removed
def how_many_to_trim(path_string):
	return len(path_string.split('/')) - 1

def get_trimmed_path(path_string, trim_num):
	path_list = path_string.split('/')
	return '/'.join(path_list[trim_num:])


# run through with recursion limit
# thanks to nosklo on stack overflow
def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)

    # ricky code:
    trim_num = how_many_to_trim(some_dir)

    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield get_trimmed_path(root,trim_num), dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

# if no path argument is specified
if len(sys.argv) == 1:
	root = os.getcwd()
# if a path is specified
else:
	root = sys.argv[1]
	if root == ".":
		root = os.getcwd()

# Now, from root, our goal is to assemble JSON like in the flare.json example.
# It should be most natural to use internal Python lists and dictionaries, and then 
# do a json.dump to get the resulting string. 


# For now, assume max recursion, with an arbitrarily large level:
level = 10

fs = walklevel(root,level)

with open("sample.txt","w") as f:
	for thing in fs:
		f.write(str(thing) + "\n")




# Here's an example of what the would happen in the first line of turning sample.txt
# into the format of flare.json: It is incomplete as is, but we will mutate this
# dictionary as necessary step-by-step walking through the tuples returned from out
# OS call.

a = {"name":"clojure-koans","children":
				[{"name":".git","children":[]},{"name":".resources","children":[]},
						{"name":"script","children":[]},{"name":"src","children":[]},
						{"name":"target","children":[]},
						".gitignore",".lein-repl-history","epl-v10.html",
						"ideaboard.txt","project.clj","README.md","sample.txt"]}


