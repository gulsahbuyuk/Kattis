"""
Author : Gülşah Büyük
Date : 1.08.2020
"""
for i in range(int(input())):

    cities = set() ##in set you cannot duplicate input

    for j in range(int(input())):
        cities.add(input())

    print(len(cities))