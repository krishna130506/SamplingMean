import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
populationMean = statistics.mean(data)
stdev = statistics.stdev(data)
print("The Population Mean is {}".format(populationMean))

def random_set_of_mean(counter):
        dataset = []
        for i in range(0,counter):
                random_index = random.randint(0,len(data))
                value = data[random_index]
                dataset.append(value)
        mean = statistics.mean(dataset)
        return(mean)

def show_fig(mean_list):
        df = mean_list
        mean = statistics.mean(mean_list)
        print("mean of sampling distribution ", mean)
        fig = ff.create_distplot([df],["reading_time"],show_hist=False)
        fig.show()


def setup():
        mean_list = []
        for i in range(0,100):
                set_of_mean = random_set_of_mean(30)
                mean_list.append(set_of_mean)
        show_fig(mean_list)
        
setup()



