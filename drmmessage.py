"""
Author : Gülşah Büyük
Date : 15.10.2020
"""
encrypted_txt = input()
letters = ['A','B','C','D','E','F','G',
           'H','I','J','K','L','M','N',
           'O','P','Q','R','S','T','U',
           'V','W','X','Y','Z']

first_half =  encrypted_txt[:-(int(len(encrypted_txt)/2))]
last_half = encrypted_txt[(int(len(encrypted_txt)/2)):]

rotate_1 = 0
rotate_2 = 0

for i in range(len(first_half)):
    rotate_1+=letters.index(first_half[i])
    rotate_2+=letters.index(last_half[i])

final = ''

for j in range(len(first_half)):
    final+= letters[(((letters.index(first_half[j])+rotate_1)%26 + (letters.index(last_half[j])+rotate_2)%26)%26)]

print(final)