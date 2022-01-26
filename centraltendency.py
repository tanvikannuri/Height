import csv
import pandas as pd
import plotly.express as px 

with open('class1.csv') as f:
    reader =csv.reader(f)
    file_data = list(reader)

    file_data.pop()

    total_marks = 0
    total_entries =len(file_data)

    for marks in file_data:
        total_marks += float(marks[1])

    mean = total_marks / total_entries
    print("Mean (Average) is ->"+str(mean)) 