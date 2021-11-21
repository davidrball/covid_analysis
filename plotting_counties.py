# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from urllib.request import urlopen
import json
import pandas as pd
import plotly
import plotly.express as px
import matplotlib.pyplot as plt
datadir = "/Users/davidrball/covid_geo/counties.json"


# =============================================================================
# 
# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#     counties = json.load(response)
# with open(datadir,'') as f:
#     json.dump(counties,f)
# =============================================================================
    

with open(datadir) as json_file:
    counties = json.load(json_file)
    

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})
#simple dataframe with fips of county and unemployment rate



fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()