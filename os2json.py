#!/usr/bin/python

# script to convert data in the sample.txt file to the form like
# flare.json, required by D3.

import re
import sys
import json

# Slurp in the tuples recovered from OS

with open('sample.txt','r') as f:
	raw_tuples = f.read()
	comma_tuples = re.sub(r'\n',',',raw_tuples)
	tuple_list = eval(''.join(["[",comma_tuples,"]"]))

def make_branch(node):
	out = {}
	# new name is at the end of the path
	out["name"] = node[0].split('/')[-1]
	# only add kids when there are any:
	if len(node[1] + node[2]) >= 1:
		out["children"] = node[1] + node[2]
	return out




# TODO
# Okay Ricky, you're close!
# What you need to do now is make sure that 




def get_ref(parent_path_list,core):

	middles = parent_path_list[1:-1]
	# initialize ref as the whole dict
	ref = core

	# find where the new name is located, and then
	# update ref accordingly, diving inward
	for name in middles:

		# this isn't pretty, but I need to recover the index 
		# of where the item with "name":name is, and some of the
		# items in the list aren't even maps
		candidate_list = ref["children"]
		new_index = None
		for j in range(len(candidate_list)):
			if type(candidate_list[j]) == dict:
				if candidate_list[j]["name"] == name:
					new_index = j

		if new_index == None:
			print "Uh-oh, we didn't find the index."
			sys.stdout.exit(1)
		
		ref = ref["children"][new_index]

	return ref




root = tuple_list[0]

core = make_branch(root)

rest = tuple_list[1:]

# Each time, we find the old stub, delete it, and replace it
# with the proper set of children.
for node in rest:
	new_branch = make_branch(node)

	parent = node[0] 
	parent_path_list = parent.split('/')
	target = parent_path_list[-1]

	ref = get_ref(parent_path_list,core)
	
	ref['children'] = [make_branch(node) if x==target else x for x in ref['children']] 


with open('sample_solved.json','w') as f:
	f.write(json.dumps(core))





# Consider:

# This line worked for a hardwired first iteration. Gets the find and replace done right.
#core['children'] = [make_branch(rest[0]) if x=='.git' else x for x in core['children']] 

# Also, you will rather annoyingly have to dive through core in an alternating
# fashion like this. 
#flare["children"][0]["children"][1]["children"][3]

# Let's recursively dive through to get ref (!) to be one above the desired list we want
# to do a replacement on. So ref['children'] will then be the list we go through to replace.

# We'll start off with ref = core. Then as we dive down, we'll make replacements of the
# form ref = ref["children"][j] as many times as necessary.





















"""
def get_parent_ref(parent_path_list,core):
	# we cut off the beginning because of initialization,
	# the end because that is what we will replace
	middles = parent_path_list[1:-1]

	key = core['name']

	for name in middles:
		try:
			key = core[key]
		except KeyError:
			print("Uh-oh, a key error.")
			sys.exit(1)
	
	# this ought to be a direct reference to the desired parent
	return key
"""




			


	


