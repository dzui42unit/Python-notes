#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# read data from a 'csv' file
# parse it and return as a dictionary
def read_csv(file_name):
	# read a content of the file and split into lines
	file_data = open(file_name).read().split('\n')
	# first line will hold the keys 
	# remove all the quotes from the string
	file_data[0] = file_data[0].replace('"', '')
	# get list of keys
	file_data_keys = file_data[0].split(';')
	# remove first string after it was processed
	file_data.pop(0)
	# extract all the data
	values = []
	for line in file_data:
		# split the line to get list of numbers
		line_split = line.split(';')
		to_add = []
		# go through each of them and add to the resulting list, convert to float
		for line_part in line_split:
			if line_part != "":
				to_add.append(float(line_part))
		# append it to the values list
		values.append(to_add)
	# create a dictionary, that will hold the values for each parameter
	data_set = {key: [] for key in file_data_keys}
	j = 0
	cols = len(data_set.items())
	for key in data_set.keys():
		col = []
		for elem in values:
			col.append(elem[j])
		j += 1
		data_set[key] = col
	return (data_set)


# function to print a graph basing on the data
def plot_graph(data, good_threshold, bad_threshold):
	
	# demo to plot two random graphs on the same line

	fig = plt.figure('Test plots')

	# first two number represent the size of imaginary grid
	# second its position
	# example of plot's indexes
	# 1 2
	# 3 4
	plot_1 = fig.add_subplot(221)
	plot_1.plot([(1, 2), (3, 4)], [(4, 3), (2, 3)])

	plot_2 = fig.add_subplot(222)
	plot_2.plot([(7, 2), (5, 3)], [(1, 6), (9, 5)])

	# print data I work with
	print(data['fixed acidity'])
	print(data['volatile acidity'])
	
	# specify range of x and y axis
	max_x = max(data['fixed acidity'])
	max_x +=  max_x * 0.15
	max_y = max(data['volatile acidity'])
	max_y += max_y * 0.15
	
	# plot the graph
	plot_3 = fig.add_subplot(223)
	plot_3.plot(data['fixed acidity'], data['volatile acidity'], 'ro')
	plot_3.axis([0, max_x, 0, max_y])


	plt.show()


# a main function to run the demo
def main():
	# read_csv('winequality-red.csv')
	data_set = read_csv('test.csv')
	plot_graph(data_set, 0, 0)
	return


if __name__ == '__main__':
	main()
	pass