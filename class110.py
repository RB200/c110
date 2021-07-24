import plotly.figure_factory as ff
import plotly.graph_objects
import statistics
import pandas as pd
import csv
import random

df=pd.read_csv('data.csv')
data=df['temp'].tolist()
mean=statistics.mean(data)
standardDeviation=statistics.stdev(data)
print(mean)
print(standardDeviation)
#fig=ff.create_distplot([data],['temp'],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode='lines',name='mean'))
#fig.show()
# The code to find mean and std deviation of 100 random data values
dataset=[]
for i in range(0,100):
    randomIndex=random.randint(0,len(data))
    value=data[randomIndex]
    dataset.append(value)
mean2=statistics.mean(dataset)
stdev=statistics.stdev(dataset)
print(mean2)
print(stdev)
# code to find the mean of 100 data points 1000 times
# pass the number of data points as counter
def randomSetOfMean(counter):
    dataset1=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset1.append(value)
    mean1=statistics.mean(dataset1)
    return mean1
    
# function to plot the mean on the graph
def show_fig(mean_list):
    df1=mean_list
    fig1=ff.create_distplot([df1],['temp'],show_hist=False)
    fig1.show()
# function to get mean of 100 data points 1000 times
def setup():
    mean_list=[]
    for i in range(0,1000):
        setOfMean=randomSetOfMean(100)
        mean_list.append(setOfMean)
    show_fig(mean_list)
setup()
def get_stdef():
    mean_list=[]
    for i in range(0,1000):
        setOfMean=randomSetOfMean(100)
        mean_list.append(setOfMean)
    stdev2=statistics.stdev(mean_list)
    print(stdev2)
get_stdef()

