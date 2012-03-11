#!/usr/bin/env python
#-*-coding:utf-8-*-

print "Adjon meg három vesszővel elválasztott számot."
nn = list(input())
max, index = nn[0], "első"

if (nn[1] > max):
	max = nn[1]
	index = "második"
if (nn[2] > max):
	max = nn[2]
	index = "harmadik"
print "A lista legnagyobb értéke a(z) ", max, ", amelyik a(z) ", index
