#! /usr/bin/python

import sys

sqrt = 0
for line in sys.stdin:
  line = line.strip()
  num = float(line)
  sqrt = num**0.5
  print sqrt

