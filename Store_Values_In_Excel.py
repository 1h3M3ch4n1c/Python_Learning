#!/usr/bin/python3

#import the openpyxl module
import openpyxl

#Create a new workbook object
objWorkbook = openpyxl.Workbook()

#Get the names of the sheets
print (objWorkbook.get_sheet_names());

#Create a sheet object
objSheet = objWorkbook.get_sheet_by_name('Sheet')

#Set the values in the cells
for iRow in range(1,10):
    for iColumn in range(1,7):
        objSheet.cell(row = iRow,column = iColumn).value = iRow

#save the Excel in the currebt direcctory
objWorkbook.save('Store_Values_In_Excel.xlsx')
