"""
Author : Gülşah Büyük
Date : 25.10.2020
"""
number = int(input())
babywords = list(map(str,input().split()))
i = 1
case = 0
for j in babywords :
    if j == str(i) :
        i+=1
    elif j == 'mumble' :
        i+=1
    else :
        case = 1
if case == 0 :
    print("makes sense")
else :
    print("something is fishy")
