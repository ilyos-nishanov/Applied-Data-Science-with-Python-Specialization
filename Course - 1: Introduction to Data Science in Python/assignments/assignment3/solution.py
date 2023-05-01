import pandas as pd
import numpy as np

Energy = pd.read_excel('assets/Energy Indicators.xls', skiprows=17, skipfooter=38, na_values='...', usecols=[2,3,4,5], names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])
