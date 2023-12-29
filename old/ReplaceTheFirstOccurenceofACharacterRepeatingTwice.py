strTestString='A New Begining'
strTestList=[x for x in strTestString]
strCheck=''
for chrEachCharacter in strTestList:
    strCheck=strCheck+chrEachCharacter
    if (strTestList.count(chrEachCharacter)>=2 and strCheck.count(chrEachCharacter)==1 and chrEachCharacter!=' '):
        strTestList[strTestList.index(chrEachCharacter)]='0'
print(''.join(strTestList))
