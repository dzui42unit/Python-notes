#!/usr/bin/env python3


# a function that adds two objects with some examples of their result
def add(a, b):
	print(a + b)
	return (a + b)


# main function to run examples
def main():
	add(5, 7)
	add(1.23, 13.54)
	add('kek', 'lol')
	add([1, 3], [4, 7, 8, 10])

if __name__ == '__main__':
	main()