"""
RECORD CHECK  -  my version
===========================

Name  :Dussaye Bhavesh Kumar
Lane  :  AI 
Date  :08/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Determine status depending on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    return "OK" 
        

def check(value, limit):
    """Calculate and return the difference and the percentage."""
    difference = value - limit
    percent = (value - limit) * 100
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


over_limit_count = 0

while True:
    label = input("Enter dataset name (or type 'quit' to stop): ") #ask user for dataset name
    if label.lower() == "quit": #convert to lowercase so typing (QUIT,Quit,quit,QuiT) all works the same
        break 
    value = float(input("Enter rows loaded: ")) #ask user for rows loaded
    limit = float(input("Enter expected rows: ")) #ask user for expected rows
    difference, percent = check(value, limit) #process the calculations
    status = status_of(percent) #check status

    if status == "OVER LIMIT": #check how many times status comes back as OVER LIMIT
        over_limit_count += 1

    print_report(label, value, limit, difference, status) #output the formatted report

print(f"Session over. Total OVER LIMIT reached: {over_limit_count}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
