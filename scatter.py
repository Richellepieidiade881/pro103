import pandas as pd
import plotly_express as px 
df=pd.read_csv("copy of data ")
fig=px.scatter(df,x="data",y="cases",color="country",size_max=30)
fig.show()