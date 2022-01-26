import plotly.express as px
import csv 
import numpy as np

def plotFigure(data_path):
  with open(data_path) as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Size of TV",y="Average Time Spent")
    fig.show()

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Size of TV"]))
            cold_drink_sales.append(float(row["Average Time Spent"]))