#!/usr/bin/env python3

# source activate my_env

import pandas as pd
import random
import itertools
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# function to print a graph basing on the data

def plot_graph(data, good_threshold, bad_threshold, save_plot=False):

	# get the number of variables to process and get know the size of scatter matrix
	numvars = len(data.keys())
	# 
	# create an figure an subplots to wotk with
	fig, axes = plt.subplots(nrows=numvars, ncols=numvars, figsize=(25,25))

	# Hide all ticks and labels for the plots on the matrix
	# where row_nb == column_nb, those are labels for the parameter
	for i in range(numvars):
		for j in range (numvars):
			axes[i, j].xaxis.set_visible(False)
			axes[i, j].yaxis.set_visible(False)
	
	# # Label the diagonal subplots, taking keys of the dict as a text for them
	for i, label in enumerate(data.keys()):
		axes[i, i].annotate(label.capitalize(), (0.5, 0.5), xycoords='axes fraction', ha='center', va='center')

	good_wine = data[data['quality'] > good_threshold]
	bad_wine = data[data['quality'] < bad_threshold]

	i = 0
	for key_1 in good_wine:
		j = 0;
		for key_2 in good_wine:
			if key_1 != key_2:
				axes[i, j].plot(good_wine[key_2], good_wine[key_1], 'g.')
			j += 1
		i += 1


	i = 0
	for key_1 in bad_wine:
		j = 0;
		for key_2 in bad_wine:
			if key_1 != key_2:
				axes[i, j].plot(bad_wine[key_2], bad_wine[key_1], 'r.')
			j += 1
		i += 1


	# # to add spacing between all the plots
	fig.tight_layout()

	# # display all the plots
	plt.show()

	if save_plot:
		fig.savefig('whine-quality-red-scatter-matrix.png')


# a main function to run the demo
def main():
	
	df = pd.read_csv("winequality-red.csv", sep=';')

	plot_graph(df, 6, 5, True)
	return


if __name__ == '__main__':
	main()
	