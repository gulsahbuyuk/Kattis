"""
Author : Gülşah Büyük
Date : 12.07.2021
"""
n = int(input())
lenght = 0
for i in range(n):
    l = int(input())
    lenght += l

tot = lenght-(n-1)
print(tot)
