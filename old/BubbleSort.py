#!/usr/bin/python3

#import random module
from random import *


def BubbleSortFunction(ListL):
    iItr = 0
    iJtr = 0
    iLen = len(ListL)
    iNumberOfComparisons = 0
    while (iItr<iLen):
        iJtr = 0
        while (iJtr<iLen-iItr-1):
            if ListL[iJtr] > ListL[iJtr+1]:
                ListL[iJtr],ListL[iJtr+1] = ListL[iJtr+1],ListL[iJtr]
            iJtr += 1
            iNumberOfComparisons += 1
        iItr += 1
    print (iNumberOfComparisons)
    return ListL
        

def main():
    #Create a List containing random elements
    ListL = [x+randint(0,100) for x in range(1,randint(3,7))]
    print (ListL)

    #Call the function BubbleSort
    newListL = BubbleSortFunction(ListL)
    print ("The sorted list is {0}".format(newListL))

if __name__ == "__main__":
    main()
