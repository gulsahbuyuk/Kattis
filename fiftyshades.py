"""
Author : Gülşah Büyük
Date : 30.07.2020
"""

cnt = 0
number=int(input())

for i in range(number):
    pinkish = input().lower()
    if "pink" in pinkish or "rose" in pinkish:
        cnt += 1

if cnt == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(cnt)