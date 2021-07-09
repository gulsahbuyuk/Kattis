"""
Author : Gülşah Büyük
Date : 17.10.2020
"""
x,y = map(int,input().split())
case = False
if y%2==0 :
    case = True
if case:
    print("possible")
else :
    print("impossible")

