"""
Author : Gülşah Büyük
Date : 29.07.2020
"""

n,h,v = [int(x) for x in input().split()]
height=4
c=[]
c=sorted([h*v*height,h*(n-v)*height,(n-h)*v*height,(n-h)*(n-v)*height])

print(c[3])






