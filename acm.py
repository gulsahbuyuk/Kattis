"""
Author : Gülşah Büyük
Date : 16.10.2020
"""
log = ''
right = []
wrong = []
rightnumbers = []

while log!='-1':
    log = input()
    if log!='-1':
        if 'right' in log.split() and not (log.split()[1] in rightnumbers):
            right.append(log.split())
            rightnumbers.append(log.split()[1])
        else:
            wrong.append(log.split())


number_of_wrong = 0

for i in right:
    for j in wrong:
        if j[1] == i[1]:
            number_of_wrong+=1


score = 20*number_of_wrong
for i in right:
    score+=int(i[0])
print(len(right),score)