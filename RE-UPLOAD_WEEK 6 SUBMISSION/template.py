"""
RECORD CHECK  -  my version
===========================

Name  : Dussaye Bhavesh
Lane  :  AI 
Date  : 03/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd #import the pandas library for data manipulation
import matplotlib.pyplot as plt #import the matplotlib library for plotting

df = pd.read_csv("ai_survey.csv") #read the CSV file into a pandas DataFrame

df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100 #calculate the percentage of rows loaded and add it as a new column

#Give each dataset a status based on its percentage
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"            
)   

print(df)
print(df[df["status"] != "OK"]) #print only the rows where the status is not "OK"
print(df.groupby("status").size()) #group the DataFrame by status and print the count of each group

df.to_csv("ai_survey_report.csv", index=False) #save the DataFrame to a new CSV file without the index

df["status"].value_counts().plot(kind="bar") #create a bar chart showing the number of each status value
plt.title("AI Dataset Status Counts") #add a title to the plot
plt.savefig("ai_status_counts.png") #save the plot as a png file
plt.show() #display the plot



