"""
Author : Gülşah Büyük
Date : 24.08.2020
"""

l,n = tuple(map(int, input().split()))
c = 1
while l % n != 0:
    c += 1
    n = n - (l % n)
print(c)