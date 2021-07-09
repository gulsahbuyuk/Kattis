"""
Author : Gülşah Büyük
Date : 4.07.2020
"""
nums=[]
for x in range(int(input())) :
    nums.append(int(input()))

if len(nums)==nums[-1] :
    print("good job")
for i in range(1,nums[-1]+1):
    if i not in nums :
        print(i)


