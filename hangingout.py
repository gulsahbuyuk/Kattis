"""
Author : Gülşah Büyük
Date : 1.08.2020
"""
room_size , loop =[int(x) for x in input().split()]

count=0
people=0

for i in range(loop) :
    condition,person = input().split()
    if condition == "enter" :
        if people + int(person) > room_size :
            count+=1
        else :
            people += int(person)
    elif condition == "leave" :
        people -= int(person)
print(count)
