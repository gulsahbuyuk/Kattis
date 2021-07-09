"""
Author : Gülşah Büyük
Date : 14.10.2020
"""
def count_digits(n):
    return sum([int(x) for x in n])

while(True):
    n = input()
    if n == "0":
        break
    multiplication = count_digits(n)
    i = 11
    while(count_digits(str(i*int(n))) != multiplication):
        i = i + 1
    print(i)