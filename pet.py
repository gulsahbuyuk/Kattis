"""
Author : Gülşah Büyük
Date : 14.10.2020
"""
high = 0
info = []
for i in range(1,6):
    score = list(map(int,input().split()))
    total = sum(score)
    if total>high:
        high = total
        info = [i,total]

print('{} {}'.format(info[0], info[1]))