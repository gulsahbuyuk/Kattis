"""
Author : Gülşah Büyük
Date : 29.07.2020
"""
day, month = [int(x) for x in input().split()]
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
firstday = [3, 6, 6, 2, 4, 0, 2, 5, 1, 3, 6, 1]
current = (firstday[month - 1] + day - 1) % 7

print(week[current])


##eğer firstday e week[3] gibi atama yazarsan hata alıyorsun string dönüyor çünkü dikkat!!