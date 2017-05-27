#!/usr/bin/python3

#import random module
from random import *


def BubbleSortFunction(ListL):
    iItr = 0
    iJtr = 0
    iTemp = 0
    iNumberOfComparisons = 0
    while (iItr<=len(ListL)-1):
        jItr = iItr+1
        while (jItr<=len(ListL)-1):
            if ListL[iItr] > ListL[jItr]:
                ListL[iItr],ListL[jItr] = ListL[jItr],ListL[iItr]
            jItr += 1
        iItr += 1
    return ListL
        

def main():
    #Create a List containing random elements
    ListL = [x+randint(0,100) for x in range(1,10)]
    print (ListL)

    #Call the function BubbleSort
    newListL = BubbleSortFunction(ListL)
    print ("The sorted list is {0}".format(newListL))

if __name__ == "__main__":
    main()
