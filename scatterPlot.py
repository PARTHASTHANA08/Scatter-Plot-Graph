import pandas as pd
import plotly.express as px 

df = pd.read_csv("covidData.csv")
fig = px.scatter(df, x = "cases", y = "date" ,size = "cases" , size_max = 65,  color = "country" , title = "Graph Showing Data Of Covid-19 ")
fig.show()