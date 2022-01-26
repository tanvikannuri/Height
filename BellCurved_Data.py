import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("Phone_Data.csv")
fig = ff.create_distplot([df["Mobile Brand"].tolist()],["Brand"],show_hist = False)
fig.show()