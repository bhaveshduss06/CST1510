"""
RECORD CHECK  -  my version
===========================

Name  : Dussaye Bhavesh
Lane  :  AI 
Date  : 04/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
    """Clean a survey record and return a dictionary."""

    raw_line = raw_line.strip().lower() #remove spaces and use lowercase
    parts = raw_line.split(",") #split the text at ","
    data ={"survey": parts[0].strip()} #store the survey name

    for part in parts[1:]: #loop through each part
        key, value = part.split("=", 1) #separate key and value

        key = key.strip() #remove extra spaces
        value = float(value.strip()) #remove spaces and convert to float
        data[key] = value #add the key and value to the dict

    return data


def status_of(data):
    """Check if the survey rating meets the standard."""

    if data["rating"] >= 4: #check if the rating is 4 or more
        return "OK"
    else:
        return "FLAGGED"
    

raw_records = [] #create an empty list

with open("survey_records.txt", "r") as file: #open the text file i created
    for line in file: #read each line
        raw_records.append(line) #add the line to the list


flagged_count = 0

for raw_record in raw_records: #loop through each record
    data = parse_line(raw_record) #clean the line
    status = status_of(data) #check the rating

    print(data, status)

    if status == "FLAGGED": #check if flagged
        flagged_count += 1 #increment the count by 1

print("Total records: ", len(raw_records))
print("Flagged records: ", flagged_count)
