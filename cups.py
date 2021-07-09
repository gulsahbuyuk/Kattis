"""
Author : Gülşah Büyük
Date : 14.10.2020
"""
cupNum = int(input())
cups = {}
for i in range(cupNum):
    line = input().split()
    if line[0].isnumeric():
        cups[int(line[0])/2] = line[1] #radius doubled if integer comes before the color
    else:
        cups[int(line[1])] = line[0]
print("\n".join([cups[k] for k in sorted(cups.keys())]))