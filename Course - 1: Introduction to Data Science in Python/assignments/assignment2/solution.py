import pandas as pd
import numpy as np

df = pd.read_csv('assets/NISPUF17.csv')
print(df.head())

# def proportion_of_education ():
#     df = pd.read_csv('assets/NISPUF17.csv')
#     df = df[['EDUC1']]
#     df = df.dropna()
#     df = df.sort_values(by=['EDUC1'])
#     df = df.groupby('EDUC1').size()
#     df = df / df.sum()
#     return df
# print(proportion_of_education())