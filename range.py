#!/usr/bin/env python3


def main():

	# creating a range
	print(range(5))
	for i in range(5):
		print(i)

	# specify a range with a start and end value
	for i in range(10, 20):
		print(i)

	# specify a range with a step value as a third argument
	for i in range(0, 10, 2):
		print(i)

	# a convinitent way to create a list of integers
	int_list = list(range(0, 10))
	print(int_list)

	# prefer using enumerate() for counters
	# enumerate() yields (index, value) tuples
	t = [6, 372, 8862, 148800, 2096886]

	for p in enumerate(t):
		print(p)

	for i, v in enumerate(t):
		print("i = {}, v = {}".format(i, v))

if __name__ == '__main__':
	main()