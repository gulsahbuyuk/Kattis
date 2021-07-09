"""
Author : Gülşah Büyük
Date : 3.07.2020
"""

numbers =[int(x) for x in input().split()]

for i in range(1,numbers[-1]+1) :
    if i%numbers[0] == 0 and i%numbers[1] != 0 :
        print("Fizz")
    elif i%numbers[0]==0 and i%numbers[1]==0:
        print("FizzBuzz")
    elif i%numbers[0] != 0and i%numbers[1]== 0 :
        print("Buzz")
    else :
        print(i)