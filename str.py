#!/usr/bin/env python3

import math

def main():
	
	string  = "This is a string"
	print(string, len(string))
	print("Concatination: " + string)
	
	# join method for contactination of the strings
	# takes a list of strings to join, applied this method to a separator

	colors = ';'.join(['#54ff23', '#2321fa', '#a322312'])
	print(colors)
	# join to an empty string to make a simple concatination
	simple_contact_str = ''.join(['one', 'two', 'three'])
	print(simple_contact_str)
	# partition devides a string into three parts around the separator
	# returns a tuple
	print("unforgetable".partition("forget"))
	# format is used to insert values to a string
	print("The age of {0} is {1}".format('Jim', 32))

	pos = (62.6, 12.42, 234.5)
	print("Position is x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos))
	print("Math contstants are pi={m.pi} e={m.e}".format(m=math))
	return

if __name__ == '__main__':
	main()