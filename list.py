#!/usr/bin/env python3


def main():

	str = "show how to index into sequences".split()

	print(str)

	print("str[4] = {}".format(str[4]))

	# get access to the element by the negative index
	# last element has index -1

	print("str[-2] = {}".format(str[-2]))

	# the way to slice a list with a positive indexes
	silce_list = str[0:5]
	print(silce_list)

	# slice a list with negative indexes
	silce_list_neg = str[1:-1]
	print(silce_list_neg)

	# a way to copy a list
	copy_list = str[:]
	not_copy = str
	copy_list[0] = 'nice try'

	print(str)
	print(copy_list)

	# another possible ways to copy a list
	copy_2 = str.copy()
	copy_3 = list(str)

	return


if __name__ == '__main__':
	main()