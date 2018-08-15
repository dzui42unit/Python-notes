#!/usr/bin/env python3


import os


def make_at(path, dir_name)
	original_path = os.getcwd()
	try:
		os.chdir(path)
		os.mkdir(dir_name)
	except OSError as e:
		print(e, file=sys.stderr)
		raise
	finally:
		# this block of code will be executed
		# no matter how the try-block exits
		os.chdir(original_path)

def main():
	return 


if __name__ == '__main__':
	main()