#!/usr/bin/env python3

from pprint import pprint as pp

def main():

	# create a list of tuples
	name_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)]

	# craete a dictionary from the the tuples list
	d = dict(name_and_ages)

	print(d)

	# cretae a dict directly passing a key value arguments
	d2 = dict(a='alpha', b='beta', c='charlie', d='delta')

	print(d2)

	# ways of copying the dictionary
	# using a copy() method
	# passing dictionary to the dict() constructor
	copy1 = d.copy()
	copy2 = dict(d)

	print(copy1)
	print(copy2)

	# update a dictionary with a new key-value pairs
	copy1.update(d2)
	print(copy1)

	# if the key already exists in the dictionary
	# its value will be replaced by the value from a 'source'

	stocks = {'GOOG': 891, 'APPL': 416, 'IMB': 194}
	stocks.update({'IBM': 200, 'YHOO': 25, 'APPL': 914})
	print(stocks)

	# iteration through the dictionary
	for key in stocks:
		print("{key} => {value}".format(key=key, value=stocks[key]))

	# efficient way to iterate through the values in the dictionary
	for value in stocks.values():
			print(value)

	# the same thing for keys
	for key in stocks.keys():
		print(key)

	# each key value pair is called item
	# tuple unpacking is used
	for key, value in stocks.items():
		print("{} => {}".format(key, value))

	# in and not in operators work only for keys in the dictionary
	# not on the values


	# sorth of the dictionary bu the keys
	test_d = {2: 3, 4: 5, 1: 3, 5: 1}
	print(test_d)
	test_d_sorted = dict(sorted(test_d.items()))
	for key, value in test_d_sorted.items():
		print("{key} => {value}", key, value)

if __name__ == '__main__':
	main()