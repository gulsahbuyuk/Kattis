"""
Author : Gülşah Büyük
Date : 4.08.2020
"""
from math import cos,pi
print((lambda t: "safe" if t[1] <= 180 else int(t[0] / cos(pi * (t[1] / 180 + 0.5))))(tuple(map(lambda x: int(x), input().split()))))

#map() function calls the specified function for each item of an iterable (such as string, list, tuple or dictionary) and returns a list of results.
#Return an iterator that applies function to every item of iterable, yielding the results.map()