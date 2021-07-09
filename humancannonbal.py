"""
Author : Gülşah Büyük
Date : 3.08.2020
"""

from math import sin,cos,radians

num = int(input())
g = 9.81

for i in range(num):
    velocity,theta,y,h1,h2 = [float(x) for x in input().split()]

    t = y/(velocity*cos(radians(theta)))

    x = velocity*t*sin(radians(theta))-0.5*g*t**2

    if x-1<=h1 or x+1>=h2:
        print("Not safe")
    else:
        print("Safe")
