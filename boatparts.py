"""
Author : Gülşah Büyük
Date : 16.10.2020
"""
parts = set()
p , n = [int(x) for x in input().split()]
for i in range(n):
    parts.add(input())
    if len(parts) == p:
        print(i + 1)
        break
else:
    print('paradox avoided')