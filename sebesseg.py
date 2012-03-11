#!/usr/bin/env python
#-*-coding:utf-8-*-

sebesseg = raw_input('Adja meg a sebességet (mérföld/h): ')
s = float(sebesseg)
km = s * 1.609
m = km / 3.6
print s, ' mérföld/h ',km, 'km/h és ',m,' m/s.'
