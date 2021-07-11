"""
Author : Gülşah Büyük
Date : 12.07.2021
"""
arr = input()
nums= arr.split(";")
tot = 0
for nums in nums :
    nums = nums.split("-")
    first = int(nums[0])
    last = int(nums[1]) if len(nums)==2 else first

    no = last - first + 1
    tot += no

print(tot)