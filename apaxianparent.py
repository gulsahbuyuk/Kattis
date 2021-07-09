"""
Author : Gülşah Büyük
Date : 1.08.2020
"""

word1,word2 = input().split()
if word1[-1] == 'a' or word1[-1] == 'i' or word1[-1] == 'o' or word1[-1] == 'u':
    print(word1[:-1] + "ex" + word2)
elif word1[-2:] == 'ex':
    print(word1+word2)
elif word1[-1] == 'e':
    print(word1+"x"+word2)
else:
    print(word1+"ex"+word2)