"""
Author : Gülşah Büyük
Date : 12.07.2021
"""

strg = input()

lowercase = 0
uppercase = 0
symbols = 0
space = 0

for case in strg:
    if case.islower():
        lowercase += 1
    elif case.isupper():
        uppercase += 1
    elif case == "_" :
        space += 1
    else :
        symbols += 1

length = len(strg)
r1 = space / length
r2 = lowercase / length
r3 = uppercase / length
r4 = symbols / length

print(r1)
print(r2)
print(r3)
print(r4)