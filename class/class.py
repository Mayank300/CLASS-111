import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import random
import plotly.graph_objects as go

df = pd.read_csv("class.csv")
data = df["Math_score"].tolist()
mean_list = []

mean = st.mean(data)
std = st.stdev(data)

print("mean => ",mean)
print("std => ",std)


def randomMean(sample_num):
    dataSet = []
    for i in range(0,sample_num):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataSet.append(value)

    mean_for_dataSet = st.mean(dataSet)
    print("{} is the mean of the dataSet".format(mean_for_dataSet))
    return mean_for_dataSet

for i in range(0,1000):
    set_of_mean = randomMean(100)
    mean_list.append(set_of_mean)
mean_for_mean_list = st.mean(mean_list)
std_for_mean_list = st.stdev(mean_list)

print("mean of sampling dist => ",mean_for_mean_list)
print("std of sampling dist => ",std_for_mean_list)
print("mean => ",mean)
print("std => ",std)

# fig = ff.create_distplot([mean_list],["Scores for mean_list"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean_for_mean_list,mean_for_mean_list], y=[0,0.20], mode="lines", name="mean"))
# fig.show()


# fig = ff.create_distplot([data],["Scores"],show_hist=False)
# fig.show()




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

z_score = (ipad_mean - mean_for_mean_list)/std_for_mean_list
print("z_score => ",z_score)


fig = ff.create_distplot([mean_list],["Scores for mean_list"],show_hist=False)


# fig.add_trace(go.Scatter(x=[ipad_mean,ipad_mean],y=[0,0.17], mode="lines", name = "MEAN"))
# fig.add_trace(go.Scatter(x=[start_num1,start_num1], y=[0,0.20], mode="lines", name="Start Std1"))
# fig.add_trace(go.Scatter(x=[end_num1,end_num1], y=[0,0.20], mode="lines", name="End Std1"))


# fig.add_trace(go.Scatter(x=[eclass_mean,eclass_mean],y=[0,0.17], mode="lines", name = "MEAN"))
# fig.add_trace(go.Scatter(x=[start_num2,start_num2], y=[0,0.20], mode="lines", name="Start Std2"))
# fig.add_trace(go.Scatter(x=[end_num2,end_num2], y=[0,0.20], mode="lines", name="End Std2"))


fig.add_trace(go.Scatter(x=[sheet_mean,sheet_mean],y=[0,0.17], mode="lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[start_num3,start_num3], y=[0,0.20], mode="lines", name="Start Std3"))
fig.add_trace(go.Scatter(x=[end_num3,end_num3], y=[0,0.20], mode="lines", name="End Std3"))



fig.show()



print("")
print("")
print("")
print("")
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
print("")
print("")
print("")
print("")



print("z_score => ",z_score)
print("")
print("")
print("")
print("")
print("")


