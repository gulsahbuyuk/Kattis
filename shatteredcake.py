"""
Author : Gülşah Büyük
Date : 12.07.2021
"""

width = int(input())
n = int(input())

area = 0
for i in range(n):
    w,l = [int(x) for x in input().split()]
    area += (w*l)

len = int(area / width)
print(len)


