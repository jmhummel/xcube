#!/usr/bin/env python

"""xcube.py: A solver for the X-Cube variation on the Rubik's cube"""

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

colors = ['red',
          'orange',
          'yellow',
          'green',
          'blue',
          'white']

class XCube():
	def __init__(self):
		self.state = []