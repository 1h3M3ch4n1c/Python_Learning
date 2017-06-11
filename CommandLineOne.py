#!/usr/bin/python3
#Command line program to count the number of
#Line in the File

#import sys module
import sys

def main():
    #Enter the command
    try:
        CommandLine = sys.argv[1]
        if CommandLine == "--help":
            print("This is a simple command line program")
        elif CommandLine == "--length":
            fileToRead = open("CommandLineOne.py","r")
            numberOfWords = len(fileToRead.read())
            fileToRead.close()
            print("Length of the file: {}".format(numberOfWords))
        elif CommandLine == "--showcontents":
            fileToRead = open("CommandLineOne.py","r")
            fileContent = fileToRead.read()
            print("File contents: \n{}".format(fileContent))
            fileToRead.close()
        else:
            print("Unrecognised command: {}".format(CommandLine))
    except (IndexError):
        print("No command entered")

if __name__ == "__main__":
    main()
