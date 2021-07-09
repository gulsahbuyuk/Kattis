"""
Author : Gülşah Büyük
Date : 6.08.2020
"""
x,y = [int(x) for x in input().split()]

while x and y:
    t = int(x/y)

    print(f"{t} {x-t*y} / {y}")


    x, y = [int(x) for x in input().split()]