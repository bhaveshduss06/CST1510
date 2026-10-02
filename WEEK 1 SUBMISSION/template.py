"""
RECORD CHECK  -  my version
===========================

Name  : DUSSAYE BHAVESH
Lane  :  AI 
Date  : 29/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

dataset_name = input("Enter dataset name: ") #ask user for dataset name
rows_loaded = int(input("Enter rows loaded: ")) #ask user for rows loaded
rows_expected = int(input("Enter expected rows: "))#ask user for expected rows

difference = rows_loaded - rows_expected        #calculation of the difference between loaded and expected rows
percentage = (rows_loaded/rows_expected) * 100  #calculation of the percentage difference of loaded and expected rows

print()
print("=" * 34)
print(f" RECORD CHECK -  {dataset_name}")
print("=" * 34)
print(f" Expected Rows: {rows_expected:>13}")
print(f" Rows Loaded  : {rows_loaded:>13}")
print(f" Difference   : {difference:>+16.2f}") #adding + sign to show whether the difference has increased or decreased
print(f" Percentage   : {percentage:>16.2f} %")
print("=" * 34)











#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
