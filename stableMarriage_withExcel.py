#! python 3
# -*- coding: utf-8 -*-
"""
Stable Marriage Problem with Gale-Shapley Algorithm
Run with Excel Input (after changing it into csv)
Save the Result as a Text file

Requirement: Save Excel-file(raw data) in \Excel_Data
"""

import stableMarriage, os, openpyxl, csv

# Locating Excel-file to process
for excelFile in os.listdir('.\Excel_Data'):
    excelFile = '.\\Excel_Data\\' + excelFile
    if excelFile.endswith('.xlsx') == False: # skip non-excel file
        continue
    # Change Excel File to CSV File
    wb = openpyxl.load_workbook(excelFile)
    for sheetName in wb.sheetnames:
        # Loop through 'Active' and 'Passive' sheets in the workbook
        sheet = wb[sheetName]
        
        # Create the CSV filename from the Excel filename and sheet title.
        csvFile = open(excelFile[:-5] + '_' + sheetName + '.csv', 'w', newline='')
        
        # Create the csv.writer object for this CSV file.
        csvWriter = csv.writer(csvFile)
        # Loop through every row in the sheet
        # except the first row
        for rowNum in range(2, sheet.max_row + 1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)
            # Write the rowData list to the CSV file.
            csvWriter.writerow(rowData)
        csvFile.close()
        
# Getting data from CSV File

# Run Algorithm

# Save result as Text file
