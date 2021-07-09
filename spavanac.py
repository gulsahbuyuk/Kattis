"""
Author : Gülşah Büyük
Date : 4.07.2020
"""
time = input().split()
hour = int(time[0])
minute = int(time[1])

alarm = minute - 45

if alarm >= 0 :
    print(f"{hour} {alarm}")
else:
    if hour== 0 :
        print(f"23 {60 + alarm}")
    else:
        print(f"{hour-1} {60 + alarm }")




