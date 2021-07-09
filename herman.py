"""
Author : Gülşah Büyük
Date : 4.07.2020
"""
from math import pi,sqrt
radius = int(input())
ratio = (2/ pi)**0.5

euclid = pi*(radius)**2
taxicab= pi*(ratio*radius)**2

print("{:.6f}".format(euclid))
print("{:.6f}".format(taxicab))

