"""
Author : Gülşah Büyük
Date : 3.08.2020
"""
nums = [int(x) for x in input().split(" ")]
rule = (nums[1]**2+nums[2]**2)**0.5

for i in range(nums[0]):
    match = int(input())
    if match<=rule:
        print("DA")
    else:
        print("NE")