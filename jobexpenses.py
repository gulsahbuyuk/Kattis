"""
Author : Gülşah Büyük
Date : 30.07.2020
"""
num = int(input())
all = [int(x) for x in input().split()]
exp = 0
for i in range(num):
    if all[i] < 0 :
        exp += all[i]

print(abs(exp))
