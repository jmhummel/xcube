#!/usr/bin/env python

"""2x2cube.py: A solver for the 2x2 variation on the Rubik's cube"""

import sys
import re
import copy

__author__     = "Jeremy Hummel"
__copyright__  = "Copyright 2016"
__credits__    = ["Jeremy Hummel"]
__license__    = "MIT"
__version__    = "1.0.0"
__maintainer__ = "Jeremy Hummel"
__email__      = "jmhummel@gmail.com"
__status__     = "Prototype"
__date__       = "2016-01-14"

class TwoXTwoCube():
	def __init__(self):
		self.state = []
		for i in range(6):
			self.state.append([[str(i),str(i)],[str(i),str(i)]])

	def __str__(self):
		s = ''
		s += '  ' + ''.join(self.state[0][0]) + '\n'
		s += '  ' + ''.join(self.state[0][1]) + '\n'
		for i in range(1, 5):
			s += ''.join(self.state[i][0])
		s += '\n'
		for i in range(1, 5):
			s += ''.join(self.state[i][1])
		s += '\n'
		s += '  ' + ''.join(self.state[5][0]) + '\n'
		s += '  ' + ''.join(self.state[5][1])
		return s

	def twist(self, face, dir):


def main():
	print TwoXTwoCube()

if __name__ == '__main__':
    main()