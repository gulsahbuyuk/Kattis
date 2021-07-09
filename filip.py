"""
Author : Gülşah Büyük
Date : 3.07.2020
"""

numbers = input().split()

for num in range(len(numbers)):
    numbers[num]=numbers[num][::-1]
if int(numbers[0]) > int(numbers[1]):
    print(numbers[0])
else:
    print(numbers[1])





