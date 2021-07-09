"""
Author : Gülşah Büyük
Date : 17.10.2020
"""
number = int(input())
faktor=1
euler=1
for i in range(1,number+1):
    faktor = faktor*i
    euler += 1/faktor
print(euler)