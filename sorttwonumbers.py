"""
Author : Gülşah Büyük
Date : 12.07.2021
"""
x,y = [int(x) for x in input().split()]

if x < y:
    print(x, " ", y)
else :
    print(y, " ", x)