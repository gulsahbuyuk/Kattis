"""
Author : Gülşah Büyük
Date : 29.07.2020
"""

decisions = int(input())


for i in range(decisions):
    nums = [int(x) for x in input().split(" ")]
    money = nums[1] - nums[2]

    if money == nums[0]:
        print("does not matter")
    elif money > nums[0]:
        print("advertise")
    elif money < nums[0]:
        print("do not advertise")