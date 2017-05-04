#!/usr/bin/python3
#import openpyxl module
import openpyxl

#create workbook object
objWorkbook = openpyxl.load_workbook('Create_Sheets_And_Remove_Sheets.xlsx')

#create dynamic sheet object
objSheetList = objWorkbook.get_sheet_names()

#remove the sheets in the loaded workbook
for iItr in range(1,len(objSheetList)):
    objWorkbook.remove_sheet(objWorkbook.get_sheet_by_name(objSheetList[iItr]))

#save the workbook
objWorkbook.save('Create_Sheets_And_Remove_Sheets.xlsx')
