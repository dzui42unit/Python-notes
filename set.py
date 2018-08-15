#!/usr/bin/env python3

def main():

	# create an set

	empty_set = set()

	# create a set from a a list
	# it is an efficient way to remove duplicates
	s = set([2, 3, 2, 2, 5, 8, 13, 56])
	print(s)

	# set is iterable, but the order is arbitary
	for elem in {1, 6, 678, 3, 12}:
		print(elem)

	# membership is checked by 'in' 'not in' operators

	# add an element to the set
	# adding of the existing element does not change the set
	# and does not cause an error
	print(s)
	s.add(66543)
	print(s)

	# to add multiple elements we can use update() method
	# any iterable series can be passed
	s.update([7, 8, 12, 45, 454, 323])
	print(s)

	# remove element from the set
	# if the element does not exist, we get an KeyError
	s.remove(7)
	print(s)

	# another way is to use discard() method
	# if the element is not a part of set
	# no error will occurr
	s.discard(1111111)

	# to copy we can use

	new_s = s.copy()

	new_s_2 = set(s)

	# examples of algebra operations on the sets

	blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
	blonde_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
	smell_hcn = {'Harry', 'Amelia'}
	taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
	o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
	b_blood = {'Amelia', 'Jack'}
	a_blood = {'Harry'}
	ab_blood = {'Joshua', 'Lola'}

	# find a union of the sets
	print(blue_eyes.union(blonde_hair))

	# find intersection of the sets
	print(blue_eyes.intersection(blonde_hair))

	# find difference of the sets
	print(blonde_hair.difference(blue_eyes))

	# symmetric difference of the sets
	print(blonde_hair.symmetric_difference(blue_eyes))

	# check if a set is a substet of some set
	print(smell_hcn.issubset(blonde_hair))

	# check if a set is a superset
	print(taste_ptc.issuperset(smell_hcn))

	# check if sets have no elements en common
	print(a_blood.isdisjoint(o_blood))

	return

if __name__ == "__main__":
	main()