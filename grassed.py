"""
Author : Gülşah Büyük
Date : 30.07.2020
"""
cost = float(input())
rep = int(input())

total = 0.

for _ in range(rep):
    w,h = [float(x) for x in input().split()]
    total += w*h*cost

print("{:.7f}".format(total))