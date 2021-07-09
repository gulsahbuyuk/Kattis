"""
Author : Gülşah Büyük
Date : 30.07.2020
"""

from math import sin,radians,ceil

h = [int(x) for x in input().split()]
ladder=ceil(h[0]/sin(radians(h[1])))
print(ladder)