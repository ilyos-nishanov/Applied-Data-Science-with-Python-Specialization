import pandas as pd
import numpy as np
import re
import warnings
warnings.filterwarnings('ignore')

Energy = pd.read_excel('assets/Energy Indicators.xls',na_values=["..."],header = None,skiprows=18,skipfooter= 38,usecols=[2,3,4,5],names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])

print (Energy.head())


# Energy['Energy Supply'] = Energy['Energy Supply'] * 1000000
# Energy['Country'] = Energy['Country'].str.replace(r" \(.*\)","")
# Energy['Country'] = Energy['Country'].str.replace(r"\d*","")

# Energy['Country'] = Energy['Country'].replace({"Republic of Korea": "South Korea",
#                                                 "United States of America": "United States",
#                                                 "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
#                                                 "China, Hong Kong Special Administrative Region": "Hong Kong"})
# Energy.set_index('Country').loc['United States']
# for i in Energy['Country'].replace({'United States of America' : 'United States',
#                                     'United Kingdom of Great Britain and Northern Ireland':'United Kingdom',
#                                     'China, Hong Kong Special Administrative Region':'Hong Kong'}):
#     print(i)
