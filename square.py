#! /usr/bin/python

import sys

square = 0
for line in sys.stdin:
  line = line.strip()
  num = float(line)
  square = num**2
  print square
  



