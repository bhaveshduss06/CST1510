"""
RECORD CHECK  -  my version
===========================

Name  :DUSSSAYE BHAVESH KUMAR
Lane  :  AI     
Date  :17/10/2026
Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Determine status of percentage."""
    if percent >=100: #Check if the percentage is 100 or more
        return "OVER LIMIT"
    elif percent >= 90: #Check if the percentage is 90 or more
        return "NEAR LIMIT"
    else: #Otherwise, the percentage is OK
        return "OK"

def check(value, limit):
    """Calculate and return difference and percentage."""
    percent = (value / limit) * 100 #Calculate percentage
    difference = value - limit #Calculate difference
    return difference, percent

def print_report(label, value, limit, difference, status): #Display the final report
    """Print the final formatted report."""
    print()
    print("=" * 34)
    print(f" RECORD CHECK -  {label}")
    print("=" * 34)
    print(f"Expected Rows  : {limit:>10.2f}")
    print(f"Loaded Rows    : {value:>10.2f}")
    print(f"Remaining Rows : {difference:>10.2f}")
    print(f"Percent        : {percent:>10.2f} %")
    print(f"Status         : {status:>10}")
    print("=" * 34)

def load_records(path):
    """Reads dataset name, loaded rows, and expected rows from a file."""
    records = []
    try:
        with open(path, "r") as file: #Open the file in reading mode
            for line in file:
                if line.strip():  #Skip empty lines
                    name, loaded, expected = line.strip().split(",") #Split the line into 3 parts
                    records.append({
                        "label": name,
                        "value": float(loaded),
                        "limit": float(expected)
                    })
    except FileNotFoundError: #Handle the error if the file is missing
        print(f"Error: The file {path} was not found.")
    return records

records = load_records("my_own_data.txt") #Load the records from the text file
over_limit_count = 0 #counter for how many items exceed the limit

with open("results.txt", "w") as f:
    for row in records:
        label, value, limit = row["label"], row["value"], row["limit"] #Get the values from the dictionary
        difference, percent = check(value, limit) #Calculate the difference and percentage
        status = status_of(percent) #Determine the status

        if status == "OVER LIMIT":
            over_limit_count += 1 #Increase the counter by 1
        print_report(label, value, limit, difference, status) #Display the report
        f.write(f"{label}, {status}\n") #Save the label and status in the file

print(f"Session over. Total OVER LIMIT reached: {over_limit_count}")

