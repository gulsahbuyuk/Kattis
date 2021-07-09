"""
Author : Gülşah Büyük
Date : 24.10.2020
"""
num2words1 = {0:'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
def Number(number) :
    if (number >= 0) and (number <= 19):
        return (num2words1[number])
    elif (number >= 20) or (number <= 99):
        tens,remainder = divmod(number,10)
        return (num2words2[tens - 2] + '-' + num2words1[remainder].lower() if remainder else num2words2[tens - 2])

line=[]
try :
    while True :
        s=input().split()
        line.append(s)
except Exception as e:
    for i in range(len(line)) :
        for j in range(len(line[i])):
            try:
                num = int(line[i][j])
                if j== 0 :
                    line[i][j] = Number(num)
                else :
                    line[i][j] = Number(num).lower()
            except:
                pass
for i in line :
    print(" ".join(i))







