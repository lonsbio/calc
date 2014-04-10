#!/usr/bin/env python
"""
A dimple calculator pakache in python

Take any number of arguments and add them as integers

"""
import sys

if __name__ == '__main__':
	command = sys.argv[1]
	nums = [int(a) for a in sys.argv[2:]]
	if (command == 'add'):
		print sum(nums)
	elif command == 'multiply':
		print reduce(lambda x, y: x * y, nums)

