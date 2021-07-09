"""
Author : Gülşah Büyük
Date : 16.10.2020
"""
n = int(input())
TB,LR = (0,)*2

for i in range (n):
    topbot,leftright = (lambda s: (s[:2].count('0'), s[2:].count('0')))(input())
    TB += topbot
    LR += leftright

sword = min(TB,LR)//2
print(f'{sword} {TB - sword*2} {LR - sword*2}')










