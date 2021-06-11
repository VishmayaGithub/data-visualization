
from typing import Sized
import pandas as pd
import plotly.express as px

d = pd.read_csv("covid.csv")
fig = px.scatter(d,x='date',y='cases',color = 'country')

fig.show()