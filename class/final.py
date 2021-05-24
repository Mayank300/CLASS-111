import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import random
import plotly.graph_objects as go

ipad_csv = pd.read_csv("ipad.csv")
ipad_data = ipad_csv["Math_score"].tolist()

eclass_csv = pd.read_csv("extra_class.csv")
eclass_data = eclass_csv["Math_score"].tolist()

sheet_csv = pd.read_csv("worksheet.csv")
sheet_data = sheet_csv["Math_score"].tolist()


ipad_mean = st.mean(ipad_data)
ipad_std = st.stdev(ipad_data)

eclass_mean = st.mean(eclass_data)
eclass_std = st.stdev(eclass_data)

sheet_mean = st.mean(sheet_data)
sheet_std = st.stdev(sheet_data)

start_num1,end_num1 = mean - std, std + mean
start_num2,end_num2 = mean - (2 * std), (2 * std) + mean
start_num3,end_num3 = mean - (3 * std), (3 * std) + mean

fig = ff.create_distplot([ipad_mean],["Scores for mean_list"],show_hist=False)
fig.add_trace(go.Scatter(x=[ipad_std,ipad_std], y=[0,0.20], mode="lines", name="mean"))
fig.show()





print("")

print("mean for ipad_mean => ",ipad_mean)
print("std for ipad_std => ",ipad_mean)

print("")

print("mean for eclass_mean => ",eclass_mean)
print("std for eclass_std => ",eclass_std)

print("")

print("mean for sheet_mean => ",sheet_mean)
print("std for sheet_std => ",sheet_std)

print("")
