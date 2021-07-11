"""
Author : Gülşah Büyük
Date : 11.07.2021
"""
n = int(input())

for i in range(n):
    arr = [int(x) for x in input().split()]
    minus = arr[0]-1
    arr.pop(0)
    sum =0
    for j in range(len(arr)):
        sum += arr[j]
    print(sum-minus)

