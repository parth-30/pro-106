import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Cups of coffee", y="Hours of sleep")
        fig.show()

def getDataSource(data_path):
    cups_of_coffee = []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))

    return {"x" : cups_of_coffee, "y": hours_of_sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between cups of coffee vs hours of sleep :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()