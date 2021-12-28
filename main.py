import plotly.figure_factory as ff 
import plotly.graph_objects as go
import statistics
import random
import pandas as pd 
import csv 
df=pd.read_csv("data1.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
stdev=statistics.stdev(data)
print("population mean is ",population_mean)
print("standard deviation is ",stdev)
def random_set_of_mean(counter):

    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    samplestdev=statistics.stdev(dataset)
    return mean
def show_fig(mean_list):
    df=mean_list
    sample_mean=statistics.mean(mean_list)
    print("mean of sampling distribution is ",sample_mean)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[sample_mean,sample_mean],y=[0,1],mode="lines",name="sample_mean"))
    fig.show()
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
def standarddeviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    std_deviation=statistics.stdev(mean_list)
    print("standard deviation of sampling distribution is ",std_deviation)
  
setup()
standarddeviation()