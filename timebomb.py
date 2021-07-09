"""
Author : Gülşah Büyük
Date : 25.10.2020
"""
asciirep = {"**** ** ** ****" : '0',
         "  *  *  *  *  *" : '1',
         "***  *****  ***" : '2',
         "***  ****  ****" : '3',
         "* ** ****  *  *" : '4',
         "****  ***  ****" : '5',
         "****  **** ****" : '6',
         "***  *  *  *  *" : '7',
         "**** ***** ****" : '8',
         "**** ****  ****" : '9',
        }
inputlist =[]
for i in range(5):
    line = input()
    ac = len(line)
    if i==0 :
        for j in range(0,ac,4) :
            inputlist.append(line[j:j + 3])
    else :
        k = 0
        for j in  range(0,ac,4):
            inputlist[k] += line[j:j +3]
            k += 1
test =""
case = True
for i in inputlist :
    try :
        test += asciirep[i]
    except:
        case = False

if case :
    if int(test)/6 == int(int(test)/6) :
        print("BEER!!")
    else :
        print("BOOM!!")
else:
    print("BOOM!!")