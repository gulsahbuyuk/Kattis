"""
Author : Gülşah Büyük
Date : 24.10.2020
"""
testcase = input()
stonew = 0
stoneb= 0
for i in range(len(testcase)) :
    if testcase[i] == 'W' :
        stonew +=1
    else :
        stoneb +=1
if stoneb == stonew :
    print('1')
else :
    print('0')

