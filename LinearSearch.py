#!/usr/bin/python3

#import the random module

from random import *

#Create a list that cotains random numbers
Lst = [x+randint(0,100) for x in range(0,10)]
print (Lst)

#Set a Flag which indicates whether the desired element is found
#or not
bElementNotFound = True
iItr = 0

#Accept the elemnt from the user
iElement = int(input("Enter the element you want to search:\n"))


#Search for the number till the elemnt is found
#Or the List reaches the other end

while bElementNotFound and iItr<len(Lst):
    if Lst[iItr] == iElement:
        bElementNotFound = False
        print ("The element {0}  is found at index {1}".format(iElement,iItr))
    else:
        bElementNotFound = True
    iItr += 1
if bElementNotFound:
    print ("The element {0} is not found".format(iElement))
