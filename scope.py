#!/usr/bin/env python3


# a gloabal variable for the module
count = 0


# function that prints a counter
def show_count():
	print("count is: ", count)


# function that sets a counter
# the global variable was no affected because the function created a local 'count' variable and chenged its value
def set_count(c):
	count = c

def set_global_count(c):
	global count
	count = c


# main function
def main():
	show_count()
	set_count(5)
	show_count()
	show_count()
	set_global_count(5)
	show_count()

if __name__ == '__main__':
	main()