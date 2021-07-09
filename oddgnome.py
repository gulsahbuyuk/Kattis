"""
Author : Gülşah Büyük
Date : 4.07.2020
"""

for x in range(int(input())):
    group =[int(y) for y in input().split()]
    group.pop(0)  #ilk elemanı listeden siler
    firstelement= group.pop(0)

    count = 1
    for i in group :
        if firstelement+1 == i :
            firstelement=i
            count +=1
        else:
            print(count+1)








