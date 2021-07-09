"""
Author : Gülşah Büyük
Date : 16.10.2020
"""

case = int (input())
for i in range(case):
    input()
    noGodzilla,noMechagodzilla = map(int,input().split())
    strenghtGod = [int(x) for x in input().split()]
    strenghtMecha = [int(x) for x in input().split()]
    strenghtGod.sort()
    strenghtMecha.sort()
    while True :
        if len(strenghtGod) == 0 or len(strenghtMecha)==0 :
            break
        if strenghtMecha[0] <= strenghtGod[0] :
            strenghtMecha.remove(strenghtMecha[0])
        else :
            strenghtGod.remove(strenghtGod[0])
    if len(strenghtMecha) == 0 :
        print("Godzilla")
    elif len(strenghtGod) == 0 :
        print("MechaGodzilla")
    else :
        print("uncertain")