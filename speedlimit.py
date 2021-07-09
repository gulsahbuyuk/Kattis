"""
Author : Gülşah Büyük
Date : 3.07.2020
"""

dataset = int(input())
while (dataset != -1) :
    times = 0
    totaldis=0
    for i in range(dataset):
        distance,time =  [int(x) for x in input().split()]
        fortime = time -times
        times = time
        totaldis += fortime * distance

    dataset = int(input())
    print(f"{totaldis} miles")
