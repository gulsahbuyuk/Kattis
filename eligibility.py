"""
Author : Gülşah Büyük
Date : 17.10.2020
"""
number = int(input())
for i in range (number):
    name,start,birth,course = map(str,input().split())
    if int(start.split('/')[0])>=2010 or int(birth.split('/')[0])>=1991:
        print(name+" eligible")
    elif int(course)>40 :
        print(name+ " ineligible")
    else :
        print(name+" coach petitions")