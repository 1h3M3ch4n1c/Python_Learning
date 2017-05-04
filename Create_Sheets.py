#!/usr/bin/python3
#import openpyxl

import openpyxl

#create a workbook object
objWorkbook = openpyxl.Workbook()

#create a sheets
iTotal = 10
for iItr in range(1,iTotal):
    objWorkbook.create_sheet(index=iItr,title = "Sheet "+str(iItr))

objWorkbook.save ('Create_Sheets_And_Remove_Sheets.xlsx')
