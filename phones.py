import plotly.figure_factory as ff
import random
import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("phones.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()


