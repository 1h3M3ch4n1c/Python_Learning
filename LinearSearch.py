#!/usr/bin/python3

#import the random module

from random import *



#Search for the number till the elemnt is found
#Or the List reaches the other end
def LinearSearch(ListL,iElement):
    #Set a Flag which indicates whether the desired element is found
    #or not
    
    bElementNotFound = True
    iItr = 0
    
    while bElementNotFound and iItr<len(ListL):
        if ListL[iItr] == iElement:
            bElementNotFound = False
            print ("The element {0}  is found at index {1}".format(iElement,iItr))
        else:
            bElementNotFound = True
        iItr += 1
    if bElementNotFound:
        print ("The element {0} is not found".format(iElement))
        AddElement = input("Do you want to add the element to the list: Yes/No?")
        if AddElement.upper() == "YES":
            ListL.append(iElement)
            print("The Elemeni {0} is added\nThe new list is{1}".format(iElement,ListL))
    
    return iItr

#main definition
def main():
    iElement = int(input("Enter the Element:"))
    
    #Create a list that cotains random numbers
    Lst = [x+randint(0,100) for x in range(0,10)]
    print (Lst)

    #Call the function
    numberOfSearches = LinearSearch(Lst,iElement)

if __name__ == "__main__":
    main()
