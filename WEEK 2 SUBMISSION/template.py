"""
RECORD CHECK  -  my version
===========================

Name  :DUSSAYE BHAVESH
Lane  :  AI  
Date  :30/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_limit_count = 0

while True:                              #use while true to run the program infinitely until specific condition is met
     dataset_name = input("Enter dataset name (or type 'quit' to stop): ") #ask user for dataset name or quit to stop
     if dataset_name.lower() == "quit" : #convert to lowercase so typing (QUIT,Quit,quit,QuiT) all works
          print("Program is terminated")
          break                          #use break to escape the loop
     rows_loaded = float(input("Enter rows loaded: ")) #ask user for rows loaded
     rows_expected = float(input("Enter expected rows: "))#ask user for expected rows

     difference = rows_loaded - rows_expected        #calculation of the difference between loaded and expected rows
     percentage = (rows_loaded/rows_expected) * 100  #calculation of the percentage difference of loaded and expected rows

     if percentage >= 100: #use if statment to meet conditions for status
         status = "OVER KILL"
         over_limit_count += 1
     elif percentage >= 90:
         status = "WARNING"
     else :               #use else for otherwise part
         status = "OK"
         
     print()
     print("=" * 34)
     print(f" RECORD CHECK -  {dataset_name}")
     print("=" * 34)
     print(f"Expected Rows  : {rows_expected:>10.2f}")
     print(f"Loaded Rows    : {rows_loaded:>10.2f}")
     print(f"Remaining Rows : {difference:>+10.2f}") #adding + sign to indicate an increase or decrease in the difference
     print(f"Percent        : {percentage:>10.2f} %")
     print(f"Status         : {status:>15}")
     print("=" * 34)
print(f"Program is over, Total OVER LIMIT reached: {over_limit_count}") #code terminates when "quit" is input

#code runs infinitely
#ask user for input(quit) again, so that dataset_name changed and loop terminates




