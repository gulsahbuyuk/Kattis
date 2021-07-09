"""
Author : Gülşah Büyük
Date : 15.10.2020
"""

area,n = [float(x) for x in input().split()]

radius = n/(3.14*2)
cagearea = 3.14 * radius**2

if cagearea >= area:
    print('Diablo is happy!')
else:
    print('Need more materials!')