
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv

df=pd.read_csv("perform.csv")
math_list=df["math score"].tolist()
math_mean=statistics.mean(math_list)
math_mode=statistics.mode(math_list)
math_median=statistics.median(math_list)
math_dev=statistics.stdev(math_list)

first_std_dev_start,first_std_dev_end=math_mean-math_dev,math_mean+math_dev
second_std_dev_start,second_std_dev_end=math_mean-(2*math_dev),math_mean+(2*math_dev)
third_std_dev_start,third_std_dev_end=math_mean-(3*math_dev),math_mean+(3*math_dev)

fig=ff.create_distplot([math_list],["math score"],show_hist=False)
fig.add_trace(go.Scatter(x=[math_mean,math_mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,0.17],mode="lines",name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.17],mode="lines",name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,0.17],mode="lines",name="standard deviation 2"))
fig.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.17],mode="lines",name="standard deviation 2"))
fig.add_trace(go.Scatter(x=[third_std_dev_start,third_std_dev_end],y=[0,0.17],mode="lines",name="standard deviation 3"))
fig.add_trace(go.Scatter(x=[third_std_dev_end,third_std_dev_end],y=[0,0.71],mode="lines",name="standard deviation 3"))

list_of_data_within_1_standard_deviation=[result for result in math_list if result > first_std_dev_start and result < first_std_dev_end]
list_of_data_within_2_standard_deviation=[result for result in math_list if result > second_std_dev_start and result < second_std_dev_end]
list_of_data_within_3_standard_deviation=[result for result in math_list if result > third_std_dev_start and result < third_std_dev_end]

print("mean of math_list is {}" .format(math_mean) )
print("median of math_list is {}" .format(math_median) )
print("mode of math_list is {}" .format(math_mode) )
print("standard deviation of math_list is {}" .format(math_dev) )

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_standard_deviation)*100.0/len(math_list)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_standard_deviation)*100.0/len(math_list)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_standard_deviation)*100.0/len(math_list)))






