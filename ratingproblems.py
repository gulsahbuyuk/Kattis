"""
Author : Gülşah Büyük
Date : 12.07.2021
"""
n, k = [int(x) for x in input().split()]
min = -3
max = 3
rate = 0
for i in range(k):
    points = int(input())
    rate += points

judge = n-k

minrate = (rate + min * judge) / n
maxrate = (rate + max * judge) / n

print(minrate," " , maxrate)