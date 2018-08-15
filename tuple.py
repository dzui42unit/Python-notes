#!/usr/bin/env python3


# function that returns min and max elements
# returns a tuple
def min_max(items):
	return (min(items), max(items))


def main():
	et = ()
	print('Empty tuple', et, type(et))
	et = ("Mono", 1243, "2222", 34.12, True)
	print(et)
	et *= 3
	print(et)

	set1 = [1, 2, 45, 656, 1254, -13]
	# tuple unpacking
	mn, mx = min_max(set1)
	print(mn, mx)

	# tuple unpacking works with arbitary nested tuples
	(a ,(b, (c, d))) = (1, (2, (3, 4)))

	print(a, b, c, d)

	# pythonic way of viable swapping
	a = 1
	b = 2
	print(a, b)
	a, b = b, a
	print(a, b)

	# checks for membership of element in the tuple
	if 2 in set1:
		print('5 is in the set1')
	if 30 not in set1:
		print('30 is no in the set2')


if __name__ == '__main__':
	main()