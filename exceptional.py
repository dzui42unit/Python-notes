"""A module for demonstrating exceptions. """

import sys

def convert(s):
	"""Convert to an integer."""
	try:
		return (int(s))
	except (ValueError, TypeError) as e:
		# statement that does nothing
		pass
		# print the exception message
		# exception object can be converted to the string objects
		print("Conversion error: {}".format(str(e)), file=sys.stderr)
		raise


def main():

	return

if __name__ == '__main__':
	main()