"""
Author : Gülşah Büyük
Date : 30.07.2020
"""

number = input()

while True:
    sum = 0 
    for i in number:
        sum += int(i)

    if int(number)%sum==0:
        print(number)
        break

    number = str(int(number)+1) ##use str because integer is not iterable

