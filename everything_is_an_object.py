#!/usr/bin/env python3

import source_1

def main():
	# will print all the attribures of the class
	print(dir(source_1))
	# will print its type
	print(type(source_1))
	# will print the type of the function, that is in the source_1 module
	print(type(source_1.fetch_words))
	# prints the name attribute of the function object
	print(source_1.fetch_words.__name__)

if __name__ == '__main__':
	main()