#!/usr/bin/env python3

import sys
import time

# function that prints id of the variable, for the debug purposes
def print_var_id(var):
	print("id is: " + str(id(var)))


# function for performing some tests with variables and its ids
def var_id_test():

	# id() - returns an unique identifier for an object

	x = 10
	y = 15

	# print id's of two variables

	print_var_id(x)
	print_var_id(y)

	x = y

	print_var_id(x)
	print_var_id(y)

	x += 2;

	print(x);
	print(y);

	print_var_id(x)
	print_var_id(y)	


# the value of the refercence is copied, not the value of the object
def var_modification_test():
	m = [9, 15, 24]
	modify(m);

	# m will be modified, because it will work with the reference to the list
	# and it means that it is capable of modifying it

	print('After a modification')
	print(m)


# function that simply appends one element to the list
def modify(mod_me):
	mod_me.append(42)
	print("mod_me = ", mod_me)


# function that takes two argument, one of which has a default value
# the function prints a message
def print_banner(message, border='-'):
	line  = border * len(message)
	print(line)
	print(message)
	print(line)


# function that shows a default time, this is its argument by default
# argv value will be set once, an will no change, can be viewed in the REPL
def show_default_time(arg=time.ctime()):
	print(arg)


# function that adds spam to the list
# the problem is, if not pass any arguments the menu list will grow
# it will append 'spam' to the menu list each time
def add_spam(menu=[]):
	menu.append('spam')
	return (menu)

# add_spam that avoids appending elements to it
def add_spam_avoid_copy(menu=None):
	if menu is None:
		menu = []
	menu.append('spam')
	return (menu)

# a main function
def main():
	print_banner(border="*", message="This is a message")
	show_default_time()


if __name__ == '__main__':
	main()