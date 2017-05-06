#! /usr/bin/python

import math
import fileinput

x = []
y = []
xSum = 0
ySum = 0
count = 0

for line in fileinput.input():
	line = line.strip()
	if line != "":
		line = float(line)
		if count % 2 == 0:
			x.append(line)
			xSum += line
		if count % 2 == 1:
			y.append(line)
			ySum += line
		count += 1

length = count / 2
xAvg = xSum / length
yAvg = ySum / length
distance = 0

for i in range(length):
	print math.floor(math.sqrt((xAvg - x[i])**2 + (yAvg - y[i])**2))
