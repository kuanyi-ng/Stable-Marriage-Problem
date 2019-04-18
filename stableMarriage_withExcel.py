#! python 3
# -*- coding: utf-8 -*-
"""
Stable Marriage Problem with Gale-Shapley Algorithm
Run with Excel Input (after changing it into csv)
Save the Result as a Text file

Requirement: Save Excel-file(raw data) in \Excel_Data
"""

import stableMarriage as sm
import os, openpyxl, csv, sys

def convert_Excel_CSV(excelFile, filePrefix):
    # Looking for the Excel file in folder
#    os.chdir('.\Excel_Data')
    # Change Excel File to CSV File
    wb = openpyxl.load_workbook(excelFile)
    print("Creating CSV File ...")
    for sheetName in wb.sheetnames:
        # Loop through 'Active' and 'Passive' sheets in the workbook
        sheet = wb[sheetName]
        
        # Create the CSV filename from the Excel filename and sheet title.    
        csvFile = open(filePrefix + '_' + sheetName + '.csv', 'w', newline='')
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
    print("CSV File created!")


#for excelFile in os.listdir('.\Excel_Data'):
#    if excelFile == filename:
#        os.chdir('.\Excel_Data')
#        # Change Excel File to CSV File
#        wb = openpyxl.load_workbook(excelFile)
#        print("Creating CSV File ...")
#        for sheetName in wb.sheetnames:
#            # Loop through 'Active' and 'Passive' sheets in the workbook
#            sheet = wb[sheetName]
#            
#            # Create the CSV filename from the Excel filename and sheet title.    
#            csvFile = open(excelFile[:-5] + '_' + sheetName + '.csv', 'w', newline='')
#            # Create the csv.writer object for this CSV file.
#            csvWriter = csv.writer(csvFile)
#            # Loop through every row in the sheet
#            # except the first row
#            for rowNum in range(2, sheet.max_row + 1):
#                rowData = []    # append each cell to this list
#                # Loop through each cell in the row.
#                for colNum in range(1, sheet.max_column + 1):
#                    # Append each cell's data to rowData.
#                    rowData.append(sheet.cell(row=rowNum, column=colNum).value)
#                # Write the rowData list to the CSV file.
#                csvWriter.writerow(rowData)
#            csvFile.close()
#        print("CSV File created!s")

def getData_active(filePrefix):
    """
    Getting data from CSV File (Active)
    Active:
        name1, preference(1), preference(2), ...
        name2, ...
        
    Active:
        name(str)
        preference: ['name']
        
    return activeGroup (list)
    """
#    os.chdir('.\Excel_Data')
    activeGroup = []
    csvFileObj = open(filePrefix + '_Active.csv')
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        name = row[0]
        preference = row[1:]
        activeGroup.append((name, preference))
    return activeGroup

def getData_passive(filePrefix):
    """
    Getting data from CSV File (Passive)
    Passive:
        name1, capacity, preference(1), preference(2), ...
        name2, capacity, ...
        
    Passive:
        name(str)
        capacity(int)
        preferences: {'name of Active': rank of Active} (dict: {keys(str), values(int)})
    """
#    os.chdir('.\Excel_Data')
    passiveGroup = []
    csvFileObj = open(filePrefix + '_Passive.csv')
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        name = row[0]
        capacity = int(row[1])
        preferences = row[2:]
        preference = {}
        for n in range(len(preferences)):
            preference[preferences.pop(0)] = n+1
        passiveGroup.append((name, preference, capacity))
    return passiveGroup

def saveResult(filePrefix, result):
    """
    name: [pairred_name]
    """
#    os.chdir('.\Excel_Data')
    resultFile = open(filePrefix + '_Match_Result.txt', 'w')
    # write result
    for passive in result:
        line = passive + ':['
        if len(result[passive]) > 1:
            for active in result[passive]:
                line += active + ' | '
        else:
            line += result[passive][0]
        line += ']\n'
        resultFile.write(line)
    resultFile.close()


# Main Program
    
# Getting the filename of Excel file from sys arguments
excelFile = sys.argv[1]
if excelFile.endswith('.xlsx') == False:
    print("It seems that the filename entered is not a valid Excel file.")
elif excelFile not in os.listdir('.\Excel_Data'):
        print("It seems like the Excel file is not in the Excel_Data directory")
else:
    print(excelFile)
    
filePrefix = excelFile.strip('.xlsx')

# Convert Excel file to CSV
os.chdir('.\Excel_Data')
convert_Excel_CSV(excelFile, filePrefix)

# Create Participants, Active, and Passive
village = sm.Participants()
activeGroup = getData_active(filePrefix)
passiveGroup = getData_passive(filePrefix)
for member in activeGroup:
    village.addActive(member[0], member[1])
for member in passiveGroup:
    village.addPassive(member[0], member[1], member[2])
# Run Algorithm
village.assign()
# Save result as Text file
saveResult(filePrefix, village.pairs)

