import pandas as pd
import numpy as np
import re

Energy = pd.read_excel('assets/Energy Indicators.xls', skiprows=17, skipfooter=38, na_values='...', usecols=[2,3,4,5], names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])
Energy['Energy Supply'] = Energy['Energy Supply'] * 1000000
Energy['Country'] = Energy['Country'].str.replace(r" \(.*\)","")
Energy['Country'] = Energy['Country'].str.replace(r"\d*","")

Energy['Country'] = Energy['Country'].replace({"Republic of Korea": "South Korea",
                                                "United States of America": "United States",
                                                "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                                "China, Hong Kong Special Administrative Region": "Hong Kong"})
Energy.set_index('Country').loc['United States']
for i in Energy['Country'].replace({'United States of America' : 'United States',
                                    'United Kingdom of Great Britain and Northern Ireland':'United Kingdom',
                                    'China, Hong Kong Special Administrative Region':'Hong Kong'}):
    print(i)