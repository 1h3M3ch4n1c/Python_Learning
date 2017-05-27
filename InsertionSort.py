#!/usr/bin/python3

#import the random module
from random import *

def InsertionSortFunction(ListL):
    #Length of the List
    iLen = len(ListL)-1

    #Set the first, last, next and marker positions
    iMarker = 0
    iNumberOfComparisons = 0

    while (iMarker<iLen):

        if ListL[iMarker]>ListL[iMarker+1]:
            ListL[iMarker],ListL[iMarker+1]=ListL[iMarker+1],ListL[iMarker]
            print (ListL)
            iNumberOfComparisons += 1
            for k in range(iMarker):
                if ListL[k] > ListL[iMarker]:
                    ListL[k],ListL[iMarker]=ListL[iMarker],ListL[k]
                print (ListL)
                iNumberOfComparisons += 1
        print ("The number of comparisons is:{0}".format(iNumberOfComparisons))
        iMarker = iMarker+1
    return ListL

    
    

def main():

    #Create a random list
    ListL = [x+randint(0,100) for x in range(1,randint(3,7))]
    print (ListL)

    #Call the insertion sort function
    newList = InsertionSortFunction(ListL)
    print (ListL)
if __name__ == "__main__":
    main()
