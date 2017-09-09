#!/usr/bin/python3
#Command line program to count the number of
#Line in the File

#import sys module
import sys
#import os module
import os
#import shutil
import shutil

def main():
    #Enter the command
    try:
        strCommand = sys.argv[1]
        strOptionOne = sys.argv[2]
        strOptionTwo = sys.argv[3]
        if strCommand == "--help":
            print("This is a simple command line program")
        elif strCommand == "--copy":
            print("copy command is entered,option is {}".format(strCommand))
            copyFile(strOptionOne,strOptionTwo)
        elif strCommand == "--move":
            print("copy command is entered,option is {}".format(strCommand))
            moveFile(strOptionOne,strOptionTwo)
        else:
            print("No reccognizable command entered")
    except (IndexError):
        print("No command entered")

def copyFile(srcSource,srcDestination):
    shutil.copyfile(srcSource,srcDestination)
    print("Copying of the file is done.")

def moveFile(srcSource,srcDestination):
    shutil.move(srcSource,srcDestination)
    print("File is moved to {}".format(srcDestination))

if __name__ == "__main__":
    main()
