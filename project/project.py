import csv
from typing import get_origin
import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import random
import plotly.graph_objects as go

dfc = pd.read_csv("project.csv") 
data = dfc["reading_time"].tolist()
mean_list = []
dataSet = []


population_mean = st.mean(data)
population_std = st.stdev(data)


start_num1,end_num1 = population_mean - population_std, population_std + population_mean
start_num2,end_num2 = population_mean - (2 * population_std), (2 * population_std) + population_mean
start_num3,end_num3 = population_mean - (3 * population_std), (3 * population_std) + population_mean


def show_graph(mean):
    fig = ff.create_distplot([mean],["Scores for mean_list"],show_hist=False)
    fig.add_trace(go.Scatter(x=[start_num1,start_num1], y=[0,10],  mode="lines", name="Mean"))
    fig.add_trace(go.Scatter(x=[start_num2,start_num2], y=[0,10],  mode="lines", name="Mean"))
    fig.add_trace(go.Scatter(x=[start_num3,start_num3], y=[0,10],  mode="lines", name="Mean"))
    fig.show()


def randomMean(counter):
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataSet.append(value)

    mean_for_dataSet = st.mean(dataSet)
    print("{} is the sample of the data".format(mean_for_dataSet))  
    
    return mean_for_dataSet


def setUp():
    for i in range(0,100):
        setOfMean = randomMean(30)
        mean_list.append(setOfMean)

    show_graph(mean_list)


# z_score = (ipad_mean - mean_for_mean_list)/std_for_mean_list


# def call ----

setUp()

# def call xxxx




# print state -----

print("{} is the mean of the data".format(population_mean))
print("{} is the standard deviation of the data".format(population_std))

# print state xxxx
