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
    if percent >=100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "NEAR LIMIT"
    else:
        return "OK"

def check(value, limit):
    """Calculate and return difference and percentage."""
    percent = (value / limit) * 100
    difference = value - limit
    return difference, percent

def print_report(label, value, limit, difference, status):
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
        with open(path, "r") as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    name, loaded, expected = line.strip().split(",")
                    records.append({
                        "label": name,
                        "value": float(loaded),
                        "limit": float(expected)
                    })
    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
    return records

records = load_records("my_own_data.txt")
over_limit_count = 0 #counter for how many items exceed the limit

with open("results.txt", "w") as f:
    for row in records:
        label, value, limit = row["label"], row["value"], row["limit"]
        difference, percent = check(value, limit)
        status = status_of(percent)

        if status == "OVER LIMIT":
            over_limit_count += 1
        print_report(label, value, limit, difference, status)
        f.write(f"{label}, {status}\n")

print(f"Session over. Total OVER LIMIT reached: {over_limit_count}")


   

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = []   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
