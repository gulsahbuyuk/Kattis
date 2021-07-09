"""
Author : Gülşah Büyük
Date : 14.10.2020
"""
participant= int(input())
winner = []
winnerUni = []
listOfWinner = ''
for i in range (participant):
    university,team = input().split()
    if university not in winnerUni:
        winnerUni.append(university)
        winner.append(university+ " "+team)

for i in range(12) :
    if i < 11:
        listOfWinner += winner[i] + '\n'
    else:
        listOfWinner+=winner[i]
print(listOfWinner)



