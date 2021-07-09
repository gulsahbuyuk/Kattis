"""
Author : Gülşah Büyük
Date : 17.10.2020
"""
num = int(input())
for i in range(num):
    line = list(map(int, input().split()))
    turtle = 0
    for k in range(1,len(line)-1):
        zturt= line[k]-line[k-1]*2
        if zturt<0:
            turtle +=0
        else:
            turtle+=zturt
    print(turtle)


