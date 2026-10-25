"""
RECORD CHECK  -  my version
===========================

Name  :DUSSAYE BHAVESH
Lane  :  AI 
Date  :21/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record:
    """A class to represent a record with a label, value, and limit."""

    def __init__(self, label, value, limit):
        """Initialize the Record with label, value, and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Returns the percentage of the limit that has been used."""
        return (self.value / self.limit) * 100

    def status(self):
            """Returns OVER LIMIT, WARNING or OK based on percent()."""
            percent = self.percent()
            if percent >= 100:
                return "OVER LIMIT"
            elif percent >= 90:
                return "WARNING"
            else:
                return "OK"

    def is_over(self):
            """Returns True if the value is over the limit, False otherwise."""
            return self.value > self.limit
            
def load_records(path):
    """Load records from a file and return a list of Record objects."""
    records = []
    with open(path, 'r') as file:
        for line in file:
            label, value, limit = line.strip().split(',')
            record = Record(label, float(value), float(limit))
            records.append(record)
    return records
    
records = load_records('my_own_data.txt')  # Load records from a file

over_limit_count = 0 #count of records over limit

for record in records:
         print()
         print("=" * 34)
         print(f" RECORD CHECK -  {record.label}")
         print("=" * 34)
         print(f"Expected Rows  : {record.limit:>10.2f}")
         print(f"Loaded Rows    : {record.value:>10.2f}")
         print(f"Remaining Rows : {record.limit - record.value:>10.2f}")
         print(f"Percent        : {record.percent():>10.2f} %")
         print(f"Status         : {record.status()  :>10}")
         print("=" * 34)
         if record.is_over():
             over_limit_count += 1
    


print(f"Total records over limit: {over_limit_count}")





# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
