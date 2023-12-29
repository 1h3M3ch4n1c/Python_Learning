iCurrent = 0
iNext = 1
iSequenceLength=int(input('Enter the length of the sequence:'))
while iSequenceLength>0:
    print(iCurrent)
    iTemp,iNext=iNext,iCurrent+iNext
    iCurrent,iTemp=iTemp,iNext
    # print(iNext)
    iSequenceLength-=1