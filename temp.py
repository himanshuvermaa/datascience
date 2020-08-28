import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("tempdata.csv")
data = df["temp"].tolist()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean:{}".format(mean))
fig = ff.create_distplot([data],["temp"],show_hist=False)
fig.show()

dataset= []
for i in range (0,100):
    random_index = random.randint(0,len(data))
    value= data[random_index]
    dataset.append(value)

mean1 = statistics.mean(dataset)
std_deviation1 = statistics.stdev(dataset)

print(mean1)
print(std_deviation1)

def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index = random.randint(0,len(data))
        value= data[random_index]
        dataset.append(value)

    mean3 = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)

    show_fig(mean_list)    

setup()
        

