#open the file
with open("IPAddresses.txt") as k:
    stringContent = k.read()

listOne = stringContent.split("\n")

listTwo = []

#split each line in listOne based on space
for strContentOne in listOne:
    listTwo.append(strContentOne.split(" "))

#take the input
hour = input("Enter the hour")

#search for the lines which contains the given hour
hourPresent = False
try:
    for strContentTwo in listTwo:
        if len(strContentTwo)!=0:
            if strContentTwo[1] == hour:
                hourPresent = True
                print (strContentTwo[0])
            if (not hourPresent):
                hourPresent = False
except IndexError:
    pass

if (not hourPresent):
    print ("The mentioned hour {0} does not exist in the file".format(hour))


