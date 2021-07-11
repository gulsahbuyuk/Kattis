"""
Author : Gülşah Büyük
Date : 11.07.2021
"""
vals = [int(x) for x in input().split()]
sum = 0
for i in range(len(vals)):
    sum += vals[i]
print(sum)
