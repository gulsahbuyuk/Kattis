"""
Author : Gülşah Büyük
Date : 1.08.2020
"""
simon = int(input())

for i in range(simon):
    say = input()

    if "Simon says" == say[:10]:
        print(say[11:])