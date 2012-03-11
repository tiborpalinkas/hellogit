#!/usr/bin/env python
#-*-coding:utf-8-*-

from math import pi,sqrt

l = raw_input("Az inga hossza: ")
l = float(l)
g = 9.81

T = 2 * pi * sqrt(l/g)
print 'Az ',l,' hosszúságú matematikai inga periódusideje: ',T
