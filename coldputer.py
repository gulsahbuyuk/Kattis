"""
Author : Gülşah Büyük
Date : 29.07.2020
"""
num=int(input())
temp = [int(x) for x in input().split()]
cnt=0

for i in range(len(temp)) :
    if temp[i] < 0 :
        cnt +=1
print(cnt)



