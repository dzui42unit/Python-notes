#!/usr/bin/env python3

def main():

	# define a list
	a = [[0, 5], [3, 7]]
	# copy a list
	b = a[:]
	print(a)
	print(b)

	# modify a[0]

	a[0] = [1, 2]
	print(a)
	print(b)

	# append element to the list b[1]
	b[1].append(4)

	print(a)
	print(b)

	# list repetition
	l = [1, 2, 3, 4]
	l_repeat = l * 4
	print(l_repeat)

	# repetition in shallow
	s = [[-1, 1]] * 5
	print(s)
	s[4].append(7)
	print(s)

	# way of finding the elements in the list
	w = "the quick brown fox jumps over the lazy dog".split()
	print(w)
	print(w.index('fox'))

	# this code will lead to ValueError
	# w.index('Ukraine')

	print(w.count('the'))

	# delete element from a list by its index
	del w[3]

	# delete element by its value
	w.remove('the')
	print(w)

	# remove of the element that does not exists
	# yields to the value error
	# w.remove('okay, sir')

	# insert the values in the list
	c = "I accidently the whole universe".split()
	print(c)
	c.insert(2, "destroyed")
	print(' '.join(c))

	# concatintaion of the lists
	l1 = [1, 2, 3]
	l2 = [4, 5]
	l3 = l1 + l2
	print(l3)

	# also we can extend the list
	l3.extend([56, 76, 12])
	print(l3)

	# a way to revesre a list
	l3.reverse()
	print(l3)

	# a way to sort a list in ascending order
	l3.sort()
	print(l3)

	# a way to sort the list in descending order
	l3.sort(reverse=True)
	print(l3)

	# a KEY argument for sort takes a function
	# for producing a sort key from an item

	h = "I am not here to do thiis kind of JOB".split()
	h.sort(key=len)
	print(h)

	# sorted() and reversed() methods returns a new list
	x = [4, 9, 2, 5, 7]
	y = sorted(x)
	print(x)
	print(y)
	z = [1, 5, 7, 3]
	# reversed returns an iterator, that is why we pass it
	# in the list constructor
	print(z)
	r = list(reversed(z))
	print(r)

	return

if __name__ == "__main__":
	main()