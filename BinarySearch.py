#!/usr/bin/python3

#Binary search program

#import the radonm module
from random import *

def BinarySearchFunction(ListL,iElement):
    
    #Set a flag to check presence of an element
    bFound = False
   
    #Compute the middle element index
    iFirst = 0
    iLast = len(ListL)-1
    
    while iFirst <= iLast and not bFound:

        iMiddle = (iFirst+iLast)//2
        #Compare it with the iElement
        if iElement == ListL[iMiddle]:
            bFound = True    
        elif iElement > ListL[iMiddle]:
            iFirst = iMiddle+1
        else:
            iLast = iMiddle-1

    if bFound:
        print ("The element {0} is found at {1} in the List\n".format(iElement,iMiddle))
        return iMiddle
    else:
        print ("The element {0} is not found\n".format(iElement))

def main():

    #Create a List containing the radnom integers
    ListL = [x+randint(0,100) for x in range(0,10)]
    
    #Elemnt ot search
    iElement = int(input("Enter the element to search:\n"))
    
    #Sort the List in ascending order
    ListL.sort()
    print (ListL)

    iFoundElement = BinarySearchFunction(ListL,iElement)   

if __name__ == "__main__":
    main()
